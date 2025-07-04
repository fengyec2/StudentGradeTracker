from PySide6.QtWidgets import QWidget
from ui_page.ui_page_class_grade import Ui_page_class_grade
from view.pages.page_class_grade_handler import PageClassGradeHandler
from common.utils import StyleSheet
from common.config import cfg


class PageClassGrade(QWidget, Ui_page_class_grade):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # ✅ 应用 Fluent 样式
        StyleSheet.PAGE_CLASS_GRADE.apply(self)
        cfg.themeChanged.connect(lambda: StyleSheet.PAGE_CLASS_GRADE.apply(self))

        self.handler = PageClassGradeHandler(self)  # init_ui 已在此处构造函数中完成
        self.btnQuery.clicked.connect(self.handler.on_query_clicked)
        self.btnRefresh.clicked.connect(self.handler.refresh)  # ✅ 添加刷新按钮绑定
