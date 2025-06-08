import os
import json
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

from common.utils import get_all_students, get_student_data, get_exam_display_name, load_exam_meta

class PageThreeHandler:
    def __init__(self, parent):
        self.parent = parent

    def load_student_list(self, model):
        """ 加载所有学生名称到列表 """
        model.clear()
        students = get_all_students()
        for student in students:
            item = QStandardItem(student['name'])
            model.appendRow(item)

    def load_student_scores(self, student_name):
        """ 加载并展示学生成绩表格 """
        student_data = get_student_data(student_name)
        if not student_data:
            return

        exams = student_data.get("exams", [])

        # ✅ 加载考试顺序并排序
        exam_order = [e["filename"] for e in load_exam_meta().get("exams_order", [])]
        exams = sorted(
            exams,
            key=lambda x: exam_order.index(x["filename"]) if x["filename"] in exam_order else float('inf')
        )

        # 获取所有科目集合（自动扩展）
        subject_set = set()
        for exam in exams:
            for subject in exam.get("subjects", []):
                subject_set.add(subject["subject"])
        subject_list = sorted(subject_set)

        # 构建表格数据（行：考试，列：科目+总排名）
        headers = ["考试名称"] + subject_list + ["年级排名"]
        table_data = []
        for exam in exams:
            row = []
            exam_display_name = get_exam_display_name(exam["filename"])
            row.append(exam_display_name)
            subject_scores = {s["subject"]: s["score"] for s in exam.get("subjects", [])}
            for subject in subject_list:
                row.append(subject_scores.get(subject, "—"))  # 无成绩用"—"
            row.append(exam.get("rank", "—"))
            table_data.append(row)

        self.display_table(headers, table_data)

    def display_table(self, headers, data):
        """ 在 tableView 上展示表格（使用 QStandardItemModel） """
        model = QStandardItemModel(len(data), len(headers), self.parent)
        model.setHorizontalHeaderLabels(headers)

        for row_index, row_data in enumerate(data):
            for col_index, value in enumerate(row_data):
                item = QStandardItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                model.setItem(row_index, col_index, item)

        self.parent.tableView.setModel(model)
        self.parent.tableView.resizeColumnsToContents()