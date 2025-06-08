from PySide6.QtWidgets import QWidget
from ui_page.ui_page_class_grade import Ui_page_class_grade
from view.pages.page_class_grade_handler import PageClassGradeHandler


class PageClassGrade(QWidget, Ui_page_class_grade):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.handler = PageClassGradeHandler(self)  # init_ui 已在此处构造函数中完成
        self.btnQuery.clicked.connect(self.handler.on_query_clicked)
        self.btnRefresh.clicked.connect(self.handler.refresh)  # ✅ 添加刷新按钮绑定
