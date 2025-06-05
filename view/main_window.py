import sys

from PySide6.QtCore import QRect
from PySide6.QtGui import QIcon
from qfluentwidgets import FluentWindow, NavigationItemPosition

from components.icon import MyIcon
from qfluentwidgets import FluentIcon as FIF
from view.pages.page_one import PageOne
from view.pages.page_two import PageTwo
from view.pages.setting_page import SettingInterface

import resource_rc


class MainWindow(FluentWindow):
    """ 主界面 """

    def __init__(self):
        super().__init__()
        if sys.platform == "darwin":
            self.navigationInterface.panel.setReturnButtonVisible(False)
            self.navigationInterface.panel.topLayout.setContentsMargins(4, 24, 4, 0)
        else:
            self.navigationInterface.setExpandWidth(150)
        # 创建子界面，实际使用时将 Widget 换成自己的子界面
        self.settingInterface = SettingInterface(self)
        self.pageOne = PageOne(self)
        self.pageTwo = PageTwo(self)
        self.init_navigation()
        self.init_window()

    def systemTitleBarRect(self, size):
        return QRect(0, 0, 75, size.height())

    def init_navigation(self):
        # 新增页面需要再此处添加
        sub_interface_list = [
            {'widget': self.pageOne, 'icon': MyIcon.CLICK, 'text': '页面一'},
            {'widget': self.pageTwo, 'icon': MyIcon.EXCEL, 'text': '页面二'}
        ]
        for item in sub_interface_list:
            self.addSubInterface(item['widget'], item['icon'], item['text'])

        self.addSubInterface(self.settingInterface, FIF.SETTING, '设置', NavigationItemPosition.BOTTOM)

    def init_window(self):
        if sys.platform != "darwin":
            self.setWindowIcon(QIcon(':/resource/images/logo.png'))
            self.setWindowTitle('学生成绩分析工具')
        self.resize(900, 700)
        # 把窗口放在屏幕中间
        self.move((self.screen().size().width() - self.width()) / 2,
                  (self.screen().size().height() - self.height()) / 2)
