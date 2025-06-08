import sys

from qfluentwidgets import StateToolTip
from qframelesswindow import FramelessDialog

from common.aes import aes_decrypt
from common.config import cfg, YEAR, AUTHOR
from common.utils import set_window_center, StyleSheet
from view.login_window.handler import LoginHandler
from ui_view.ui_login_window import Ui_Dialog


class LoginWindow(FramelessDialog):
    def __init__(self):
        super().__init__()
        self.stateTooltip = None
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        set_window_center(self)
        self.handler = LoginHandler(self)
        self.titleBar.raise_()
        self.init_checkbox()
        self.bind_event()
        self.ui.copyright.setText('© Copyright' + f" {YEAR}, {AUTHOR}")

        StyleSheet.LOGIN.apply(self)
        if sys.platform == "darwin":
            print("macOS detected, using system title bar.")
            self.setSystemTitleBarButtonVisible(True)
            self.titleBar.closeBtn.hide()

    def init_checkbox(self):
        self.ui.username.setText(cfg.user.value)
        p = aes_decrypt(cfg.password.value)
        if p != '':
            self.ui.password.setText(p)
            self.ui.remember.setChecked(True)
            self.ui.session.setChecked(cfg.auto_login.value)

    def bind_event(self):
        def link_checkbox(remember_click):
            if (not remember_click) and self.ui.session.isChecked():
                self.ui.remember.setChecked(True)
            if remember_click and (not self.ui.remember.isChecked()):
                self.ui.session.setChecked(False)

        self.ui.login.clicked.connect(self.handler.login)
        self.ui.getCode.clicked.connect(self.handler.get_sms_code)
        self.ui.session.clicked.connect(lambda: link_checkbox(False))
        self.ui.remember.clicked.connect(lambda: link_checkbox(True))
        self.ui.image.clicked.connect(self.handler.get_captcha)

    def showEvent(self, event):
        pass

    def loading(self, loading):
        if loading:
            if self.stateTooltip is None:
                self.stateTooltip = StateToolTip('加载中', '请耐心等待', self)
                self.stateTooltip.show()
                self.__move_tooltip()
        else:
            if self.stateTooltip is not None:
                self.stateTooltip.setTitle('操作完成')
                self.stateTooltip.setContent('')
                self.stateTooltip.setState(isDone=True)
                self.stateTooltip = None

    def __move_tooltip(self):
        if self.stateTooltip:
            tl_x, tl_y, width, height = self.window().frameGeometry().getRect()
            width2 = self.stateTooltip.width()
            self.stateTooltip.move(width - width2 - 30, 30)
