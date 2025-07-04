from PySide6.QtWidgets import QWidget
from common.utils import show_dialog, StyleSheet
from common.config import cfg
from components.bar import ProgressInfoBar
from ui_page.ui_page_top_in_grade import Ui_page_top_in_grade
from view.pages.page_top_in_grade_handler import PageTopInGradeHandler

class PageTopInGrade(QWidget, Ui_page_top_in_grade):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.loading_bar = None
        self.setupUi(self)

        # 应用 Fluent 样式
        StyleSheet.PAGE_TOP_IN_GRADE.apply(self)
        cfg.themeChanged.connect(lambda: StyleSheet.PAGE_TOP_IN_GRADE.apply(self))
        
        self.handler = PageTopInGradeHandler(self)

    def show_state_tooltip(self, title, content):
        self.loading_bar = ProgressInfoBar(title, content, self)
        self.loading_bar.show()

    def close_state_tooltip(self):
        if self.loading_bar:
            self.loading_bar.hide()
            self.loading_bar = None

    def on_common_error(self, msg):
        show_dialog(self, msg, '提示')

    # 新增的刷新方法（可选）
    def refresh(self):
        self.handler.init_exam_list()
        self.handler.init_class_list()
