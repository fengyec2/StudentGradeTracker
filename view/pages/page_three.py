from PySide6.QtWidgets import QWidget

from ui_page.ui_page_three import Ui_page_three


# 从ui文件生成的Ui_page_one类继承
class PageThree(QWidget, Ui_page_three):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
