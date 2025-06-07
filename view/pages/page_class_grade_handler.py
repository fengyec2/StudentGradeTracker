import os
import json
from collections import defaultdict

from PySide6.QtWidgets import QTableWidgetItem, QListWidgetItem, QVBoxLayout
from PySide6.QtCharts import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis
from PySide6.QtGui import QPainter

from common.utils import show_dialog, get_student_data


class PageClassGradeHandler:
    def __init__(self, ui):
        self.ui = ui

    def init_ui(self):
        # 填充考试下拉框
        meta_path = "data/exam_meta.json"
        if os.path.exists(meta_path):
            with open(meta_path, "r", encoding="utf-8") as f:
                meta = json.load(f)
                for exam in meta.get("exams_order", []):
                    display = exam.get("display_name")
                    filename = exam.get("filename")
                    self.ui.comboExam.addItem(display, userData=filename)

        # 动态收集班级列表
        class_set = set()
        student_dir = "data/students"
        for file in os.listdir(student_dir):
            if file.endswith(".json"):
                path = os.path.join(student_dir, file)
                with open(path, "r", encoding="utf-8") as f:
                    student = json.load(f)
                    class_set.add(student.get("class"))

        self.ui.listClasses.clear()
        for cls in sorted(class_set, key=lambda x: int(x) if x.isdigit() else x):
            item = QListWidgetItem(f"{cls}班")
            item.setData(0x0100, cls)  # Qt.UserRole
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

        student_dir = "data/students"
        results = defaultdict(lambda: defaultdict(list))  # class -> subject -> [score]

        for file in os.listdir(student_dir):
            if file.endswith(".json"):
                path = os.path.join(student_dir, file)
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
        # 清空旧图表
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
