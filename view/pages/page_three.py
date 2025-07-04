from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItemModel
from ui_page.ui_page_three import Ui_page_three
from view.pages.page_three_handler import PageThreeHandler
from common.utils import StyleSheet
from common.config import cfg


class PageThree(QWidget, Ui_page_three):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # ✅ 应用 Fluent 风格样式
        StyleSheet.PAGE_THREE.apply(self)
        cfg.themeChanged.connect(lambda: StyleSheet.PAGE_THREE.apply(self))

        self.handler = PageThreeHandler(self)
        self.student_model = QStandardItemModel(self.listView)
        self.listView.setModel(self.student_model)

        # 按钮点击事件：刷新学生列表
        self.pushButton.clicked.connect(self.on_import_button_clicked)

        # 学生选中事件：展示成绩表
        self.listView.clicked.connect(self.on_student_selected)

    def on_import_button_clicked(self):
        self.handler.load_student_list(self.student_model)

    def on_student_selected(self, index):
        student_name = self.student_model.itemFromIndex(index).text()
        self.handler.load_student_scores(student_name)
