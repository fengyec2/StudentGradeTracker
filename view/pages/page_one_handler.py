import os
import json
import shutil
import pandas as pd
from datetime import datetime

from PySide6.QtCore import QObject, QAbstractListModel, Qt, QModelIndex
from PySide6.QtWidgets import (
    QFileDialog, QDialog, QVBoxLayout, QLabel, QMessageBox,
    QLineEdit, QDateEdit, QPushButton, QHBoxLayout, QInputDialog
)
from PySide6.QtGui import QStandardItemModel, QStandardItem

from common.utils import show_dialog
# from workers.TaskManager import task_manager

DATA_DIR = "data"
EXAMS_DIR = os.path.join(DATA_DIR, "exams")
STUDENTS_DIR = os.path.join(DATA_DIR, "students")
META_PATH = os.path.join(DATA_DIR, "exam_meta.json")


class ExamListModel(QAbstractListModel):
    def __init__(self, exams):
        super().__init__()
        self.exams = exams

    def data(self, index: QModelIndex, role):
        if role == Qt.DisplayRole:
            return self.exams[index.row()]['display_name']

    def rowCount(self, parent=QModelIndex()):
        return len(self.exams)

    def get_exam(self, row):
        return self.exams[row] if 0 <= row < len(self.exams) else None


class ExamEditDialog(QDialog):
    def __init__(self, display_name='', real_date=None):
        super().__init__()
        self.setWindowTitle("编辑考试信息")

        self.name_input = QLineEdit(display_name)
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(real_date or datetime.now())

        layout = QVBoxLayout()
        layout.addWidget(QLabel("考试别名："))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("考试日期："))
        layout.addWidget(self.date_input)

        buttons = QHBoxLayout()
        ok_btn = QPushButton("确认")
        cancel_btn = QPushButton("取消")
        ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        buttons.addWidget(ok_btn)
        buttons.addWidget(cancel_btn)

        layout.addLayout(buttons)
        self.setLayout(layout)

    def get_data(self):
        return self.name_input.text(), self.date_input.date().toPython()


class PageOneHandler(QObject):
    def __init__(self, parent: 'PageOne'):
        super().__init__(parent)
        self._parent = parent
        self._exam_model = None
        self._parent.listView.clicked.connect(self.on_exam_selected)
        self.load_exam_list()
        self._parent.pushButton.setText("导入考试")
        self._parent.pushButton.clicked.connect(self.import_exam)
        self._parent.btnEditExamName.clicked.connect(self.edit_exam_name)
        self._parent.btnEditExamDate.clicked.connect(self.edit_exam_date)
        self._parent.btnDelete.clicked.connect(self.delete_exam)

    def load_exam_list(self):
        if not os.path.exists(META_PATH):
            self._exam_model = ExamListModel([])
        else:
            with open(META_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                exams = sorted(data["exams_order"], key=lambda e: e["real_date"], reverse=True)
                self._exam_model = ExamListModel(exams)
        self._parent.listView.setModel(self._exam_model)

    def import_exam(self):
        filepath, _ = QFileDialog.getOpenFileName(self._parent, "选择考试 Excel 文件", "", "Excel 文件 (*.xlsx)")
        if not filepath:
            return

        try:
            df = pd.read_excel(filepath)
        except Exception as e:
            show_dialog(self._parent, f"读取 Excel 文件失败：{e}")
            return

        required_columns = {"姓名", "级名", "班级"}
        if not required_columns.issubset(set(df.columns)):
            show_dialog(self._parent, "Excel 中必须包含 '姓名'、'级名' 和 '班级' 三列")
            return

        preview_info = {
            "subjects": len([col for col in df.columns if col not in ["姓名", "级名", "班级", "考试编号"]]),
            "students": df.shape[0]
        }

        dialog = ExamEditDialog()
        if dialog.exec() != QDialog.Accepted:
            return

        display_name, real_date = dialog.get_data()
        filename = f"{display_name}_{real_date.strftime('%Y-%m')}.xlsx"
        saved_path = os.path.join(EXAMS_DIR, filename)
        os.makedirs(EXAMS_DIR, exist_ok=True)
        shutil.copy(filepath, saved_path)

        os.makedirs(STUDENTS_DIR, exist_ok=True)
        for _, row in df.iterrows():
            name = row["姓名"]
            student_class = str(row.get("班级", "")).strip()
            rank = row.get("级名", None)
            subjects = [
                {"subject": col, "score": row[col], "rank": None}
                for col in df.columns if col not in ["姓名", "级名", "班级"]
            ]
            student_path = os.path.join(STUDENTS_DIR, f"{name}.json")

            if os.path.exists(student_path):
                with open(student_path, "r", encoding="utf-8") as f:
                    student_data = json.load(f)
            else:
                student_data = {"student": name, "class": student_class, "exams": []}

            if "class" not in student_data or not student_data["class"]:
                student_data["class"] = student_class

            student_data["exams"].append({
                "filename": filename,
                "real_date": real_date.strftime("%Y-%m-%d"),
                "subjects": subjects,
                "rank": int(rank) if pd.notna(rank) else None
            })

            with open(student_path, "w", encoding="utf-8") as f:
                json.dump(student_data, f, ensure_ascii=False, indent=2)

        if os.path.exists(META_PATH):
            with open(META_PATH, "r", encoding="utf-8") as f:
                meta = json.load(f)
        else:
            meta = {"exams_order": []}

        meta["exams_order"].append({
            "filename": filename,
            "display_name": display_name,
            "real_date": real_date.strftime("%Y-%m-%d")
        })

        with open(META_PATH, "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)

        self.load_exam_list()

    def on_exam_selected(self, index):
        self._selected_index = index.row()
        exam = self._exam_model.get_exam(index.row())
        if not exam:
            return

        self._parent.labelExamName.setText(exam.get("display_name", ""))
        self._parent.labelExamDate.setText(exam.get("real_date", ""))

        filepath = os.path.join(EXAMS_DIR, exam["filename"])
        try:
            df = pd.read_excel(filepath)
            self.show_excel_in_table(df)
        except Exception as e:
            show_dialog(self._parent, f"读取考试文件失败：{e}")

    def show_excel_in_table(self, df: pd.DataFrame):
        model = QStandardItemModel()
        model.setColumnCount(len(df.columns))
        model.setHorizontalHeaderLabels([str(c) for c in df.columns])
        for row in df.itertuples(index=False):
            items = [QStandardItem(str(cell)) for cell in row]
            model.appendRow(items)
        self._parent.tableView.setModel(model)

    def edit_exam_name(self):
        if not hasattr(self, "_selected_index"):
            show_dialog(self._parent, "请先选择一个考试")
            return

        exam = self._exam_model.get_exam(self._selected_index)
        if not exam:
            return

        new_name, ok = QInputDialog.getText(self._parent, "修改考试名称", "请输入新的考试名称：", text=exam["display_name"])
        if not ok or not new_name.strip():
            return

        self.update_exam_meta(exam["filename"], new_display_name=new_name.strip())

    def edit_exam_date(self):
        if not hasattr(self, "_selected_index"):
            show_dialog(self._parent, "请先选择一个考试")
            return

        exam = self._exam_model.get_exam(self._selected_index)
        if not exam:
            return

        dialog = ExamEditDialog(display_name=exam["display_name"], real_date=datetime.strptime(exam["real_date"], "%Y-%m-%d"))
        if dialog.exec() == QDialog.Accepted:
            _, new_date = dialog.get_data()
            self.update_exam_meta(exam["filename"], new_real_date=new_date.strftime("%Y-%m-%d"))

    def update_exam_meta(self, filename, new_display_name=None, new_real_date=None):
        if not os.path.exists(META_PATH):
            show_dialog(self._parent, "考试元数据文件不存在")
            return

        with open(META_PATH, "r", encoding="utf-8") as f:
            meta = json.load(f)

        changed = False
        for exam in meta.get("exams_order", []):
            if exam["filename"] == filename:
                if new_display_name:
                    exam["display_name"] = new_display_name
                    changed = True
                if new_real_date:
                    exam["real_date"] = new_real_date
                    changed = True
                break

        if changed:
            with open(META_PATH, "w", encoding="utf-8") as f:
                json.dump(meta, f, ensure_ascii=False, indent=2)
            self.load_exam_list()
            if hasattr(self, "_selected_index"):
                self._parent.listView.setCurrentIndex(self._exam_model.index(self._selected_index))
                self.on_exam_selected(self._exam_model.index(self._selected_index))
    
    def delete_exam(self):
        if not hasattr(self, "_selected_index"):
            show_dialog(self._parent, "请先选择一个考试")
            return

        exam = self._exam_model.get_exam(self._selected_index)
        if not exam:
            return

        confirm = QMessageBox.question(
            self._parent,
            "确认删除",
            f"确定要删除考试：{exam['display_name']}？该操作无法恢复！",
            QMessageBox.Yes | QMessageBox.No
        )


        if confirm != QMessageBox.Yes:
            return

        filename = exam["filename"]

        # 1. 删除 EXCEL 文件
        exam_path = os.path.join(EXAMS_DIR, filename)
        if os.path.exists(exam_path):
            try:
                os.remove(exam_path)
            except Exception as e:
                show_dialog(self._parent, f"删除考试文件失败：{e}")
                return

        # 2. 删除元数据
        try:
            with open(META_PATH, "r", encoding="utf-8") as f:
                meta = json.load(f)
            meta["exams_order"] = [e for e in meta["exams_order"] if e["filename"] != filename]
            with open(META_PATH, "w", encoding="utf-8") as f:
                json.dump(meta, f, ensure_ascii=False, indent=2)
        except Exception as e:
            show_dialog(self._parent, f"更新考试元数据失败：{e}")
            return

        # 3. 删除学生 JSON 中对应考试记录
        for file in os.listdir(STUDENTS_DIR):
            if not file.endswith(".json"):
                continue
            path = os.path.join(STUDENTS_DIR, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    student = json.load(f)
                new_exams = [e for e in student.get("exams", []) if e.get("filename") != filename]
                if len(new_exams) < len(student.get("exams", [])):
                    student["exams"] = new_exams
                    with open(path, "w", encoding="utf-8") as f:
                        json.dump(student, f, ensure_ascii=False, indent=2)
            except Exception:
                continue  # 忽略错误

        show_dialog(self._parent, f"已删除考试：{exam['display_name']}")
        self.load_exam_list()
        self._parent.labelExamName.setText("")
        self._parent.labelExamDate.setText("")
        self._parent.tableView.setModel(QStandardItemModel())
