from PIL.ImageQt import QPixmap
from PySide6.QtCore import QObject, QByteArray, Qt
from PySide6.QtGui import QBitmap, QPainter, QColor

from api.api import demo_api
from common.aes import aes_encrypt
from common.config import cfg
from qfluentwidgets import qconfig

from common.utils import show_dialog
from workers.TaskManager import task_manager


class LoginHandler(QObject):

    def __init__(self, parent: "LoginWindow"):
        super().__init__(parent)
        self._parent = parent

    def login(self):
        username = self._parent.ui.username.text()
        password = self._parent.ui.password.text()
        graphic = self._parent.ui.graphic.text()
        code = self._parent.ui.code.text()
        # 判断是否合法
        check_list = [username, password, graphic, code]
        if '' in check_list:
            return show_dialog(self._parent, content='请认真填写登录信息！', title="提示")
        try:
            self._parent.loading(True)
            task_manager.submit_task(demo_api.login, args=(username, password, graphic, code),
                                     on_success=self.on_login_success, on_error=self.on_common_error)
        except RuntimeError as e:
            self._parent.loading(False)
            show_dialog(self.parent(), content=str(e), title='出错了')

    def on_login_success(self):
        # 保存账户密码
        username = self._parent.ui.username.text()
        qconfig.set(cfg.user, username)
        if self._parent.ui.remember.isChecked():
            password = self._parent.ui.password.text()
            qconfig.set(cfg.password, aes_encrypt(password))
            qconfig.set(cfg.save_password, True)
        else:
            qconfig.set(cfg.password, '')
            qconfig.set(cfg.save_password, False)
        # 保存登录状态设置
        qconfig.set(cfg.auto_login, self._parent.ui.session.isChecked())
        self._parent.ui.login.setEnabled(False)
        self._parent.loading(False)
        self._parent.accept()

    def on_login_failed(self, msg, title='提示'):
        self._parent.loading(False)
        show_dialog(self._parent, content=msg, title=title)

    def get_captcha(self):
        try:
            task_manager.submit_task(demo_api.get_captcha, on_success=self.on_get_captcha_success,
                                     on_error=self.on_common_error)
            self._parent.loading(True)
        except RuntimeError as e:
            self._parent.loading(False)
            show_dialog(self._parent, content=str(e), title='出错了')

    def on_get_captcha_success(self, img):
        self._parent.loading(False)
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray.fromBase64(img['data'].encode()))
        # 把pixmap缩放到image的大小
        pixmap = pixmap.scaled(self._parent.ui.image.size())
        self._parent.ui.image.setPixmap(pixmap)
        size = self._parent.ui.image.size()
        mask = QBitmap(size)
        painter = QPainter(mask)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        painter.fillRect(0, 0, size.width(), size.height(), Qt.GlobalColor.white)
        painter.setBrush(QColor(0, 0, 0))
        painter.drawRoundedRect(0, 0, size.width(), size.height(), 4, 4)
        painter.end()
        self._parent.ui.image.setMask(mask)

    def get_sms_code(self):
        show_dialog(self._parent, content="获取短信验证码操作", title="测试")

    def on_common_error(self, msg, title='提示'):
        self._parent.loading(False)
        show_dialog(self._parent, content=msg, title=title)
