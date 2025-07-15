import os
from PySide6.QtCore import QStringListModel, Qt
from PySide6.QtWidgets import QVBoxLayout, QMessageBox
from PySide6.QtCharts import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis
from PySide6.QtGui import QPainter, QFont

from common.utils import load_exam_meta, get_all_students, get_student_data

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
        meta = load_exam_meta()
        # 倒序显示（最新在上）
        exams = sorted(meta.get("exams_order", []), key=lambda e: e["real_date"], reverse=True)

        exam_names = [exam["display_name"] for exam in exams]
        self.exam_mapping = {exam["display_name"]: exam["filename"] for exam in exams}

        self.exam_model = QStringListModel(exam_names)
        self.view.listView.setModel(self.exam_model)

    def init_class_list(self):
        class_set = set()
        students = get_all_students()
        for student_info in students:
            student_name = student_info.get("name")
            student_data = get_student_data(student_name)
            if not student_data:
                continue
            cls = student_data.get("class", "").strip()
            if cls:
                class_set.add(cls)
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

        students = get_all_students()
        for student_info in students:
            student_name = student_info.get("name")
            student = get_student_data(student_name)
            if not student:
                continue
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

        if not top_in_class or not top_in_grade:
            QMessageBox.information(self.view, "提示", "未能找到对应数据")
            return

        all_subjects = sorted(set(top_in_class.keys()).union(top_in_grade.keys()))
        class_scores = [top_in_class.get(subj, 0) for subj in all_subjects]
        grade_scores = [top_in_grade.get(subj, 0) for subj in all_subjects]

        self.draw_chart(all_subjects, class_scores, grade_scores)

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
        set_class = QBarSet(f"{self.view.comboBoxClass.currentText()}班总分第一")
        set_grade = QBarSet("年级总分第一")

        set_class.append(class_scores)
        set_grade.append(grade_scores)

        # 设置柱子颜色
        set_class.setColor(Qt.blue)
        set_grade.setColor(Qt.red)

        series = QBarSeries()
        series.append(set_class)
        series.append(set_grade)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(f"考试【{self.view.listView.currentIndex().data()}】总分第一成绩对比")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # 创建坐标轴
        axis_x = QBarCategoryAxis()
        axis_x.append(subjects)
        
        axis_y = QValueAxis()
        # 设置Y轴范围，留出空间显示数值标签
        max_score = max(max(class_scores) if class_scores else 0, max(grade_scores) if grade_scores else 0)
        axis_y.setRange(0, max_score * 1.1)  # 增加10%的空间
        
        chart.addAxis(axis_x, Qt.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        # 显示中文字体（微软雅黑）
        font = QFont("微软雅黑", 10)
        chart.setTitleFont(font)
        axis_x.setLabelsFont(font)
        axis_y.setLabelsFont(font)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # 连接信号以添加数值标签
        series.hovered.connect(lambda status, index, barset: self.on_bar_hovered(status, index, barset, chart_view))
        
        # 添加数值标签
        self.add_value_labels(chart_view, series, subjects, class_scores, grade_scores)

        layout.addWidget(chart_view)

    def add_value_labels(self, chart_view, series, subjects, class_scores, grade_scores):
        """在柱状图上添加数值标签"""
        from PySide6.QtWidgets import QLabel
        from PySide6.QtCore import QTimer
        
        # 使用定时器确保图表完全渲染后再添加标签
        QTimer.singleShot(100, lambda: self._add_labels_delayed(chart_view, series, subjects, class_scores, grade_scores))

    def _add_labels_delayed(self, chart_view, series, subjects, class_scores, grade_scores):
        """延迟添加标签的实际实现"""
        from PySide6.QtWidgets import QLabel
        from PySide6.QtCore import QPoint
        from PySide6.QtGui import QFont
        
        chart = chart_view.chart()
        
        # 为班级总分第一的柱子添加标签
        for i, score in enumerate(class_scores):
            if score > 0:
                label = QLabel(str(int(score)), chart_view)
                label.setAlignment(Qt.AlignCenter)
                label.setFont(QFont("微软雅黑", 8))
                label.setStyleSheet("color: blue; background-color: rgba(255, 255, 255, 180); border-radius: 3px; padding: 2px;")
                
                # 计算标签位置
                bar_rect = chart.plotArea()
                bar_width = bar_rect.width() / len(subjects)
                x = bar_rect.x() + (i + 0.25) * bar_width
                y = bar_rect.y() + bar_rect.height() - (score / (max(max(class_scores) if class_scores else 0, max(grade_scores) if grade_scores else 0) * 1.1)) * bar_rect.height() - 20
                
                label.move(int(x), int(y))
                label.show()

        # 为年级总分第一的柱子添加标签
        for i, score in enumerate(grade_scores):
            if score > 0:
                label = QLabel(str(int(score)), chart_view)
                label.setAlignment(Qt.AlignCenter)
                label.setFont(QFont("微软雅黑", 8))
                label.setStyleSheet("color: red; background-color: rgba(255, 255, 255, 180); border-radius: 3px; padding: 2px;")
                
                # 计算标签位置
                bar_rect = chart.plotArea()
                bar_width = bar_rect.width() / len(subjects)
                x = bar_rect.x() + (i + 0.75) * bar_width
                y = bar_rect.y() + bar_rect.height() - (score / (max(max(class_scores) if class_scores else 0, max(grade_scores) if grade_scores else 0) * 1.1)) * bar_rect.height() - 20
                
                label.move(int(x), int(y))
                label.show()

    def on_bar_hovered(self, status, index, barset, chart_view):
        """处理柱子悬停事件"""
        if status:
            # 可以在这里添加更多的交互效果
            pass