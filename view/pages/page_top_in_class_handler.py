import os
import json
from common.utils import get_all_students, get_student_data, load_exam_meta, get_exam_display_name
from PySide6.QtCore import QObject, QStringListModel


class PageTopInClassHandler(QObject):
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.exam_meta = load_exam_meta()

    def init_exam_list(self):
        exam_names = [item["display_name"] for item in self.exam_meta["exams_order"]]
        model = QStringListModel()
        model.setStringList(exam_names)
        self.view.examListView.setModel(model)

    def update_class_list_for_exam(self, exam_display_name):
        exam_filename = self.get_filename_by_display_name(exam_display_name)
        class_set = set()
        for student in get_all_students():
            data = get_student_data(student["name"])
            if any(exam["filename"] == exam_filename for exam in data["exams"]):
                class_set.add(data["class"])
        sorted_classes = sorted(list(class_set), key=lambda x: int(x))
        self.view.classComboBox.clear()
        self.view.classComboBox.addItems(sorted_classes)

    def load_top_subject_data(self, exam_display_name, class_name):
        exam_filename = self.get_filename_by_display_name(exam_display_name)

        class_top = {}
        grade_top = {}

        for student in get_all_students():
            data = get_student_data(student["name"])
            student_class = data.get("class")
            for exam in data["exams"]:
                if exam["filename"] != exam_filename:
                    continue
                for subject in exam["subjects"]:
                    name = subject["subject"]
                    score = subject["score"]
                    # 年级 top
                    if name not in grade_top or score > grade_top[name]:
                        grade_top[name] = score
                    # 班级 top
                    if student_class == class_name:
                        if name not in class_top or score > class_top[name]:
                            class_top[name] = score

        subject_names = sorted(set(grade_top.keys()) | set(class_top.keys()))
        class_scores = [class_top.get(subject, 0) for subject in subject_names]
        grade_scores = [grade_top.get(subject, 0) for subject in subject_names]

        self.view.update_chart(subject_names, class_scores, grade_scores)

    def get_filename_by_display_name(self, display_name):
        for exam in self.exam_meta["exams_order"]:
            if exam["display_name"] == display_name:
                return exam["filename"]
        return display_name
