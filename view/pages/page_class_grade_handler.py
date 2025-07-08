import os
import json
from collections import defaultdict

from PySide6.QtWidgets import QTableWidgetItem, QListWidgetItem, QVBoxLayout
from PySide6.QtCharts import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis
from PySide6.QtGui import QPainter
# from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex

from common.utils import show_dialog, load_exam_meta, ExamListModel  # ✅ 替代 json+路径硬编码
# from view.pages.page_one_handler import ExamListModel  # ✅ 复用模型类

DATA_DIR = "data"
STUDENTS_DIR = os.path.join(DATA_DIR, "students")
# META_PATH = os.path.join(DATA_DIR, "exam_meta.json")


class PageClassGradeHandler:
    def __init__(self, ui):
        self.ui = ui
        self._exam_model = None
        self.init_ui()

    def init_ui(self):
        self.refresh()
    
    def refresh(self):
        """刷新考试下拉框和班级列表"""
        self.load_exam_list()
        self.load_class_list()

    def load_exam_list(self):
        """采用统一模型方式加载考试列表"""
        try:
            meta = load_exam_meta()
            exams = sorted(meta.get("exams_order", []), key=lambda e: e["real_date"])
            self._exam_model = ExamListModel(exams)
        except Exception as e:
            show_dialog(self.ui, f"加载考试元数据失败：{e}")
            self._exam_model = ExamListModel([])

        self.ui.comboExam.clear()
        for i in range(self._exam_model.rowCount()):
            exam = self._exam_model.get_exam(i)
            self.ui.comboExam.addItem(exam["display_name"], userData=exam["filename"])


        # 手动绑定 QComboBox（QComboBox 不支持 setModel 默认展示）
        self.ui.comboExam.clear()
        for i in range(self._exam_model.rowCount()):
            exam = self._exam_model.get_exam(i)
            self.ui.comboExam.addItem(exam["display_name"], userData=exam["filename"])

    def load_class_list(self):
        """动态加载学生班级列表，如果目录不存在则创建"""
        if not os.path.exists(STUDENTS_DIR):
            os.makedirs(STUDENTS_DIR, exist_ok=True)

        class_set = set()
        for file in os.listdir(STUDENTS_DIR):
            if file.endswith(".json"):
                try:
                    with open(os.path.join(STUDENTS_DIR, file), "r", encoding="utf-8") as f:
                        student = json.load(f)
                        cls = student.get("class", "").strip()
                        if cls:
                            class_set.add(cls)
                except Exception:
                    continue  # 忽略无法解析的学生文件

        self.ui.listClasses.clear()
        for cls in sorted(class_set, key=lambda x: int(x) if x.isdigit() else x):
            item = QListWidgetItem(f"{cls}班")
            item.setData(0x0100, cls)
            item.setSelected(True)
            self.ui.listClasses.addItem(item)


    def on_query_clicked(self):
        selected_exam_index = self.ui.comboExam.currentIndex()
        if selected_exam_index < 0:
            show_dialog(self.ui, "请选择考试")
            return

        filename = self.ui.comboExam.currentData()
        selected_classes = [item.data(0x0100) for item in self.ui.listClasses.selectedItems()]
        if not selected_classes:
            show_dialog(self.ui, "请选择班级")
            return

        results = defaultdict(lambda: defaultdict(list))  # class -> subject -> [score]
        for file in os.listdir(STUDENTS_DIR):
            if file.endswith(".json"):
                path = os.path.join(STUDENTS_DIR, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        student = json.load(f)
                        student_class = student.get("class")
                        if student_class not in selected_classes:
                            continue
                        for exam in student.get("exams", []):
                            if exam.get("filename") == filename:
                                for subj in exam.get("subjects", []):
                                    subject = subj.get("subject")
                                    score = subj.get("score", 0)
                                    results[student_class][subject].append(score)
                except Exception:
                    continue

        # 计算平均分
        table_data = []
        subject_set = set()
        for cls, subj_scores in results.items():
            row = {"班级": f"{cls}班"}
            total = 0
            count = 0
            for subj, scores in subj_scores.items():
                avg = round(sum(scores) / len(scores), 2) if scores else 0
                row[subj] = avg
                total += sum(scores)
                count += len(scores)
                subject_set.add(subj)
            row["平均分"] = round(total / count, 2) if count else 0
            table_data.append(row)

        self.populate_table(table_data, subject_set)
        self.populate_chart(table_data, subject_set)

        # 年级平均分
        all_avg = [row["平均分"] for row in table_data if "平均分" in row]
        grade_avg = round(sum(all_avg) / len(all_avg), 2) if all_avg else 0
        self.ui.labelStats.setText(f"年级平均分：{grade_avg}")

    def populate_table(self, data, subjects):
        headers = ["班级"] + sorted(subjects) + ["平均分"]
        self.ui.tableScores.clear()
        self.ui.tableScores.setColumnCount(len(headers))
        self.ui.tableScores.setHorizontalHeaderLabels(headers)
        self.ui.tableScores.setRowCount(len(data))
        for row_idx, row in enumerate(data):
            for col_idx, key in enumerate(headers):
                val = row.get(key, "")
                item = QTableWidgetItem(str(val))
                self.ui.tableScores.setItem(row_idx, col_idx, item)

    def populate_chart(self, data, subjects):
        layout = self.ui.widgetChart.layout()
        if layout:
            while layout.count():
                child = layout.takeAt(0)
                widget = child.widget()
                if widget:
                    widget.deleteLater()
        else:
            layout = QVBoxLayout(self.ui.widgetChart)
            self.ui.widgetChart.setLayout(layout)

        subjects = sorted(subjects)
        series = QBarSeries()
        for row in data:
            bar_set = QBarSet(row["班级"])
            for subj in subjects:
                bar_set.append(row.get(subj, 0))
            series.append(bar_set)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("各班级各科平均分")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        axis = QBarCategoryAxis()
        axis.append(subjects)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        layout.addWidget(chart_view)
