import os
import json
from PySide6.QtWidgets import QMessageBox, QWidget
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis, QCategoryAxis
from PySide6.QtGui import QPainter, QStandardItem
from PySide6.QtCore import QPointF, Qt
from common.my_logger import my_logger as logger
from common.utils import show_dialog, get_all_students, get_student_data, get_exam_display_name

DATA_DIR = "data"
EXAM_META_PATH = os.path.join(DATA_DIR, "exam_meta.json")


class PageTwoHandler:
    def __init__(self, ui):
        self.ui = ui

    def load_exam_meta(self):
        try:
            with open(EXAM_META_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.exception(e)
            show_dialog(parent=None, content=f'无法读取考试元数据:{e}')
            return {"exams_order": []}

    def load_student_list(self, model):
        model.clear()
        for student in get_all_students():
            model.appendRow(QStandardItem(student["name"]))
        self.exam_meta = self.load_exam_meta()

    def plot_student_ranks(self, student_name):
        student_data = get_student_data(student_name)
        if not student_data:
            show_dialog(parent=None, content=f'未找到或读取学生文件失败：{student_name}')
            return

        exams = student_data.get("exams", [])
        filename_order = [e["filename"] for e in self.exam_meta.get("exams_order", [])]
        sorted_exams = sorted(
            exams,
            key=lambda x: filename_order.index(x["filename"]) if x["filename"] in filename_order else -1
        )

        series = QLineSeries()
        axis_x = QCategoryAxis()
        axis_y = QValueAxis()
        axis_y.setTitleText("年级排名")
        axis_y.setLabelFormat("%d")
        axis_y.setRange(0, 1000)

        point_list = []

        for i, exam in enumerate(sorted_exams):
            filename = exam["filename"]
            rank = exam.get("rank", None)
            if rank is None:
                continue
            display_name = get_exam_display_name(filename)
            point = QPointF(i, rank)
            series.append(point)
            axis_x.append(display_name, i)
            point_list.append(rank)

        if not point_list:
            show_dialog(parent=None, content='该学生暂无可绘制的排名数据')
            return

        max_rank = max(point_list)
        axis_y.setRange(0, max(max_rank + 50, 100))
        axis_y.setReverse(True)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(f"{student_name} - 年级排名变化图")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_x)
        series.attachAxis(axis_y)
        chart.legend().hide()

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        chart_layout = self.ui.chartWidget.layout()
        while chart_layout.count():
            item = chart_layout.takeAt(0)
            if item.widget():
                item.widget().setParent(None)

        chart_layout.addWidget(chart_view)
