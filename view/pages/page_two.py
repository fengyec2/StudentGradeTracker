from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItemModel # , QStandardItem
from ui_page.ui_page_two import Ui_page_two
from view.pages.page_two_handler import PageTwoHandler
from common.utils import StyleSheet
from common.config import cfg


class PageTwo(QWidget, Ui_page_two):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # ✅ 应用 Fluent 样式
        StyleSheet.PAGE_TWO.apply(self)
        cfg.themeChanged.connect(lambda: StyleSheet.PAGE_TWO.apply(self))

        self.handler = PageTwoHandler(self)
        self.pushButton.clicked.connect(self.on_import_button_clicked)

        # 初始化学生列表
        self.student_model = QStandardItemModel(self.listView)
        self.listView.setModel(self.student_model)


        # 绑定选中信号
        self.listView.clicked.connect(self.on_student_selected)

    def on_student_selected(self, index):
        student_name = self.student_model.itemFromIndex(index).text()
        self.handler.plot_student_ranks(student_name)
    
    def on_import_button_clicked(self):
        """ 手动刷新数据，点击按钮时调用 """
        self.handler.load_student_list(self.student_model)
        