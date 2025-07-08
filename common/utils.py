import os
import json

from enum import Enum
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt
from qfluentwidgets import Theme, Dialog, StyleSheetBase, qconfig
from common.my_logger import my_logger as logger

EXAM_META_PATH = os.path.join("data", "exam_meta.json")

class StyleSheet(StyleSheetBase, Enum):
    """ Style sheet  """

    WINDOW = "main_window"
    LOGIN = "login_window"
    SETTINGS = "setting_interface"
    PAGE_ONE = "page_one"
    PAGE_TWO = "page_two"
    PAGE_THREE = "page_three"
    PAGE_CLASS_GRADE = "page_class_grade"
    PAGE_TOP_IN_CLASS = "page_top_in_class"
    PAGE_TOP_IN_GRADE = "page_top_in_grade"

    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f":/resource/qss/{theme.value.lower()}/{self.value}.qss"


def show_dialog(parent, content, title='提示', url=None, callback=None):
    w = Dialog(title, content, parent)
    w.contentLabel.setOpenExternalLinks(True)
    if url:
        w.contentLabel.mousePressEvent = lambda e: QDesktopServices.openUrl(url)
    max_height = 400
    if parent:
        max_height = parent.screen().availableGeometry().height() * 0.5
    w.contentLabel.setMaximumHeight(max_height * 0.5)
    # w.contentLabel.setMinimumWidth(240)
    w.windowTitleLabel.hide()
    if not callback:
        w.yesButton.hide()
        w.cancelButton.setText('确定')
        w.buttonLayout.insertWidget(0, QLabel(''))
        w.buttonLayout.setStretch(0, 1)
        w.buttonLayout.setStretch(1, 1)
    if w.exec():
        if callback:
            callback()
    else:
        pass


def set_window_center(window):
    """ set window center """
    qr = window.frameGeometry()
    cp = window.screen().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


# Utility functions to handle student data and exam metadata


def get_all_students():
    student_dir = "data/students"
    students = []
    for filename in os.listdir(student_dir):
        if filename.endswith(".json"):
            with open(os.path.join(student_dir, filename), "r", encoding="utf-8") as f:
                data = json.load(f)
                students.append({"name": data["student"]})
    return students


def get_student_data(student_name):
    path = os.path.join("data/students", f"{student_name}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    

def load_exam_meta():
    try:
        with open(EXAM_META_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logger.exception(e)
        return {"exams_order": []}


def get_exam_display_name(filename):
    meta_path = "data/exam_meta.json"
    if not os.path.exists(meta_path):
        return filename
    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)
        for exam in meta.get("exams_order", []):
            if exam["filename"] == filename:
                return exam["display_name"]
    return filename


class ExamListModel(QAbstractListModel):
    """
    通用考试列表模型，适用于绑定考试元数据列表到 QListView 等视图。
    """

    def __init__(self, exams=None):
        super().__init__()
        self.exams = exams if exams is not None else []

    def data(self, index: QModelIndex, role):
        if role == Qt.DisplayRole and index.isValid():
            return self.exams[index.row()]['display_name']

    def rowCount(self, parent=QModelIndex()):
        return len(self.exams)

    def get_exam(self, row):
        if 0 <= row < len(self.exams):
            return self.exams[row]
        return None