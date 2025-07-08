import sys

from PySide6.QtCore import Qt, QTranslator
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication

from common.config import cfg
from common.my_logger import my_logger as logger
from common.utils import show_dialog
from view.main_window import MainWindow

# 适配缩放比例
QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
app = QApplication(sys.argv)
font = app.font()
font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
app.setFont(font)
app.setAttribute(Qt.ApplicationAttribute.AA_DontCreateNativeWidgetSiblings)  # 解决弹dialog后frameless窗口无法在调整大小
translator = QTranslator()
translator.load(":/resource/i18n/zh.qm")
app.installTranslator(translator)
app.setStyleSheet("*:focus { outline: none; }")


def main():
    logger.debug('直接进入主页面')
    main_window = MainWindow()
    main_window.show()
    app.exec()


try:
    main()
except Exception as e:
    logger.exception(e)
    show_dialog(parent=None, content='程序出现异常，请尝试重新运行！')