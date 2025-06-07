import os
import json
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis, QCategoryAxis
from PySide6.QtGui import QPainter, QStandardItem
from PySide6.QtCore import QPointF, Qt
from common.my_logger import my_logger as logger
from common.utils import show_dialog

DATA_DIR = "data"
STUDENT_DIR = os.path.join(DATA_DIR, "students")
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
        for filename in os.listdir(STUDENT_DIR):
            if filename.endswith(".json"):
                student_name = os.path.splitext(filename)[0]
                model.appendRow(QStandardItem(student_name))
        self.exam_meta = self.load_exam_meta()

    def plot_student_ranks(self, student_name):
        filepath = os.path.join(STUDENT_DIR, f"{student_name}.json")
        if not os.path.exists(filepath):
            show_dialog(parent=None, content=f'未找到学生文件：{student_name}')
            return

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                student_data = json.load(f)
        except Exception as e:
            logger.exception(e)
            show_dialog(parent=None, content=f'读取学生数据失败：{e}')
            return

        exams = student_data.get("exams", [])
        exam_display_map = {
            exam["filename"]: exam["display_name"]
            for exam in self.exam_meta.get("exams_order", [])
        }

        # 根据 exam_meta 中的顺序排序
        filename_order = [e["filename"] for e in self.exam_meta.get("exams_order", [])]
        sorted_exams = sorted(
            exams,
            key=lambda x: filename_order.index(x["filename"]) if x["filename"] in filename_order else -1
        )

        # 创建折线图数据
        series = QLineSeries()
        axis_x = QCategoryAxis()
        axis_y = QValueAxis()
        axis_y.setTitleText("年级排名")
        axis_y.setLabelFormat("%d")
        axis_y.setRange(0, 1000)  # 默认范围，可动态调整

        point_list = []

        for i, exam in enumerate(sorted_exams):
            filename = exam["filename"]
            rank = exam.get("rank", None)
            if rank is None:
                continue
            display_name = exam_display_map.get(filename, filename)
            point = QPointF(i, rank)
            series.append(point)
            axis_x.append(display_name, i)
            point_list.append(rank)

        if not point_list:
            show_dialog(parent=None, content='该学生暂无可绘制的排名数据')
            return

        max_rank = max(point_list)
        axis_y.setRange(0, max(max_rank + 50, 100))

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(f"{student_name} - 年级排名变化图")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        chart.legend().hide()

        # 清空旧图表并显示新图表
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        layout = self.ui.verticalLayout_2
        while layout.count() > 1:  # 保留前两个按钮
            item = layout.takeAt(1)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        layout.addWidget(chart_view)
