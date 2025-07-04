import os
import json
from PySide6.QtCore import QStringListModel, Qt
from PySide6.QtWidgets import QVBoxLayout, QMessageBox
from PySide6.QtCharts import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis
from PySide6.QtGui import QPainter, QFont

DATA_DIR = "data"
STUDENTS_DIR = os.path.join(DATA_DIR, "students")
EXAM_META_PATH = os.path.join(DATA_DIR, "exam_meta.json")

class PageTopInClassHandler:
    def __init__(self, view):
        self.view = view
        self.exam_model = None

        self.init_exam_list()
        self.init_class_list()
        self.view.listView.clicked.connect(self.on_exam_selected)
        self.view.comboBoxClass.currentIndexChanged.connect(self.on_class_selected)

    def init_exam_list(self):
        # 加载考试列表，填充左侧 QListView
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
        # 从学生文件收集班级列表
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
        # 默认选第一个班级
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

        # 加载所有学生数据，找出班级单科王和年级单科王
        subject_max_in_class = {}
        subject_max_in_grade = {}

        for file in os.listdir(STUDENTS_DIR):
            if not file.endswith(".json"):
                continue
            path = os.path.join(STUDENTS_DIR, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    student = json.load(f)
                student_class = student.get("class")
                exams = student.get("exams", [])
                for exam in exams:
                    if exam.get("filename") != exam_filename:
                        continue
                    for subj in exam.get("subjects", []):
                        subject = subj.get("subject")
                        score = subj.get("score", 0)
                        # 记录年级最高分
                        if subject not in subject_max_in_grade or score > subject_max_in_grade[subject]:
                            subject_max_in_grade[subject] = score
                        # 记录班级最高分
                        if student_class == class_name:
                            if subject not in subject_max_in_class or score > subject_max_in_class[subject]:
                                subject_max_in_class[subject] = score
            except Exception:
                continue

        # 准备图表数据：科目列表，班级第一，年级第一
        subjects = sorted(set(subject_max_in_class.keys()).union(subject_max_in_grade.keys()))
        class_scores = [subject_max_in_class.get(subj, 0) for subj in subjects]
        grade_scores = [subject_max_in_grade.get(subj, 0) for subj in subjects]

        self.draw_chart(subjects, class_scores, grade_scores)

    def draw_chart(self, subjects, class_scores, grade_scores):
        # 清理旧图表
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

        # 创建柱状图数据
        set_class = QBarSet(f"{self.view.comboBoxClass.currentText()}班第一")
        set_grade = QBarSet("年级第一")

        set_class.append(class_scores)
        set_grade.append(grade_scores)

        series = QBarSeries()
        series.append(set_class)
        series.append(set_grade)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(f"考试【{self.view.listView.currentIndex().data()}】班级单科王表现")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        axis = QBarCategoryAxis()
        axis.append(subjects)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        # 显示中文字体（微软雅黑）
        font = QFont("微软雅黑", 10)
        chart.setTitleFont(font)
        axis.setLabelsFont(font)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        layout.addWidget(chart_view)
