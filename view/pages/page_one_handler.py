import os
import json
import shutil
import pandas as pd
from datetime import datetime

from PySide6.QtCore import QObject, QAbstractListModel, Qt, QModelIndex
from PySide6.QtWidgets import QFileDialog, QInputDialog, QDialog, QVBoxLayout, QLabel, QLineEdit, QDateEdit, QPushButton, QHBoxLayout
from PySide6.QtGui import QStandardItemModel, QStandardItem

from common.utils import show_dialog
from workers.TaskManager import task_manager


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
            return self.exams[index.row()]["display_name"]

    def rowCount(self, parent=QModelIndex()):
        return len(self.exams)

    def get_exam(self, row):
        return self.exams[row] if 0 <= row < len(self.exams) else None


class ImportDialog(QDialog):
    def __init__(self, preview_info):
        super().__init__()
        self.setWindowTitle("导入考试信息")

        self.name_input = QLineEdit()
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(datetime.now())

        layout = QVBoxLayout()
        layout.addWidget(QLabel("考试别名："))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("考试日期："))
        layout.addWidget(self.date_input)

        layout.addWidget(QLabel(f"科目数：{preview_info['subjects']}"))
        layout.addWidget(QLabel(f"学生数：{preview_info['students']}"))

        buttons = QHBoxLayout()
        self.ok_btn = QPushButton("确认")
        self.cancel_btn = QPushButton("取消")
        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)
        buttons.addWidget(self.ok_btn)
        buttons.addWidget(self.cancel_btn)

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

        if "姓名" not in df.columns or "级名" not in df.columns:
            show_dialog(self._parent, "Excel 中必须包含 '姓名' 和 '级名' 两列")
            return

        preview_info = {
            "subjects": len(df.columns) - 2,  # 排除“姓名”和“级名”
            "students": df.shape[0]
        }

        dialog = ImportDialog(preview_info)
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
            rank = row.get("级名", None)
            subjects = [
                {"subject": col, "score": row[col], "rank": None}
                for col in df.columns if col not in ["姓名", "级名"]
            ]
            student_path = os.path.join(STUDENTS_DIR, f"{name}.json")
            if os.path.exists(student_path):
                with open(student_path, "r", encoding="utf-8") as f:
                    student_data = json.load(f)
            else:
                student_data = {"student": name, "exams": []}

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
        exam = self._exam_model.get_exam(index.row())
        if not exam:
            return
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
