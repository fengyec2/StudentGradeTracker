import os
import json
from PySide6.QtCore import QStringListModel, Qt
from PySide6.QtWidgets import QVBoxLayout, QMessageBox
from PySide6.QtCharts import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis
from PySide6.QtGui import QPainter, QFont

DATA_DIR = "data"
STUDENTS_DIR = os.path.join(DATA_DIR, "students")
EXAM_META_PATH = os.path.join(DATA_DIR, "exam_meta.json")


class PageTopInGradeHandler:
    def __init__(self, view):
        self.view = view
        self.exam_model = None

        self.init_exam_list()
        self.init_class_list()
        self.view.listView.clicked.connect(self.on_exam_selected)
        self.view.comboBoxClass.currentIndexChanged.connect(self.on_class_selected)

    def init_exam_list(self):
        try:
            with open(EXAM_META_PATH, "r", encoding="utf-8") as f:
                meta = json.load(f)
            exams = sorted(meta.get("exams_order", []), key=lambda e: e["real_date"])
        except Exception:
            exams = []

        exam_names = [exam["display_name"] for exam in exams]
        self.exam_mapping = {exam["display_name"]: exam["filename"] for exam in exams}

        self.exam_model = QStringListModel(exam_names)
        self.view.listView.setModel(self.exam_model)

    def init_class_list(self):
        class_set = set()
        if os.path.exists(STUDENTS_DIR):
            for file in os.listdir(STUDENTS_DIR):
                if file.endswith(".json"):
                    try:
                        with open(os.path.join(STUDENTS_DIR, file), "r", encoding="utf-8") as f:
                            student = json.load(f)
                            cls = student.get("class", "").strip()
                            if cls:
                                class_set.add(cls)
                    except Exception:
                        continue
        classes = sorted(class_set, key=lambda x: int(x) if x.isdigit() else x)
        self.view.comboBoxClass.clear()
        self.view.comboBoxClass.addItems(classes)

    def on_exam_selected(self, index):
        exam_name = self.exam_model.data(index, Qt.DisplayRole)
        if not exam_name:
            return
        if self.view.comboBoxClass.count() > 0:
            self.view.comboBoxClass.setCurrentIndex(0)
        self.update_chart_for(exam_name, self.view.comboBoxClass.currentText())

    def on_class_selected(self, index):
        if index < 0:
            return
        exam_indexes = self.view.listView.selectedIndexes()
        if not exam_indexes:
            return
        exam_name = self.exam_model.data(exam_indexes[0], Qt.DisplayRole)
        class_name = self.view.comboBoxClass.currentText()
        self.update_chart_for(exam_name, class_name)

    def update_chart_for(self, exam_name, class_name):
        if not exam_name or not class_name:
            return

        exam_filename = self.exam_mapping.get(exam_name)
        if not exam_filename:
            QMessageBox.warning(self.view, "错误", f"找不到考试文件对应的元数据: {exam_name}")
            return

        top_in_class = None
        top_in_grade = None
        highest_class_total = -1
        highest_grade_total = -1

        for file in os.listdir(STUDENTS_DIR):
            if not file.endswith(".json"):
                continue
            path = os.path.join(STUDENTS_DIR, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    student = json.load(f)
                student_class = student.get("class", "")
                exams = student.get("exams", [])
                for exam in exams:
                    if exam.get("filename") != exam_filename:
                        continue
                    subjects = exam.get("subjects", [])
                    total_score = sum(subj.get("score", 0) for subj in subjects)

                    if student_class == class_name and total_score > highest_class_total:
                        highest_class_total = total_score
                        top_in_class = {subj["subject"]: subj["score"] for subj in subjects}

                    if total_score > highest_grade_total:
                        highest_grade_total = total_score
                        top_in_grade = {subj["subject"]: subj["score"] for subj in subjects}
            except Exception:
                continue

        if not top_in_class or not top_in_grade:
            QMessageBox.information(self.view, "提示", "未能找到对应数据")
            return

        all_subjects = sorted(set(top_in_class.keys()).union(top_in_grade.keys()))
        class_scores = [top_in_class.get(subj, 0) for subj in all_subjects]
        grade_scores = [top_in_grade.get(subj, 0) for subj in all_subjects]

        self.draw_chart(all_subjects, class_scores, grade_scores)

    def draw_chart(self, subjects, class_scores, grade_scores):
        layout = self.view.widgetChart.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
        else:
            layout = QVBoxLayout(self.view.widgetChart)
            self.view.widgetChart.setLayout(layout)

        set_class = QBarSet(f"{self.view.comboBoxClass.currentText()}班总分第一")
        set_grade = QBarSet("年级总分第一")

        set_class.append(class_scores)
        set_grade.append(grade_scores)

        series = QBarSeries()
        series.append(set_class)
        series.append(set_grade)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(f"考试【{self.view.listView.currentIndex().data()}】总分第一成绩对比")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        axis = QBarCategoryAxis()
        axis.append(subjects)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        font = QFont("微软雅黑", 10)
        chart.setTitleFont(font)
        axis.setLabelsFont(font)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        layout.addWidget(chart_view)
