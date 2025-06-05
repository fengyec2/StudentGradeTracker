# coding:utf-8
from PySide6.QtCore import Qt, QUrl, Signal
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget, QLabel
from qfluentwidgets import FluentIcon as FIcon, CustomColorSettingCard, setThemeColor, InfoBarPosition, qconfig
from qfluentwidgets import (SettingCardGroup, OptionsSettingCard, PrimaryPushSettingCard, ScrollArea,
                            ExpandLayout, InfoBar, setTheme)

from common.config import cfg, FEEDBACK_URL, VERSION, YEAR, AUTHOR
from common.utils import StyleSheet, show_dialog
from components.icon import MyIcon


class SettingInterface(ScrollArea):
    logout = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._parent = parent
        self.setObjectName("setting_interface")
        self.scrollWidget = QWidget()

        self.expandLayout = ExpandLayout(self.scrollWidget)
        # setting label
        self.settingLabel = QLabel("设置", self)
        self.settingLabel.setObjectName('settingLabel')

        # account settings removed

        # application
        self.aboutGroup = SettingCardGroup('关于', self.scrollWidget)
        self.themeCard = OptionsSettingCard(
            cfg.themeMode,
            FIcon.BRUSH,
            "应用主题", "调整你的应用外观",
            texts=[
                self.tr('Light'), self.tr('Dark'),
                self.tr('Use system setting')
            ],
            parent=self.aboutGroup
        )
        self.themeColorCard = CustomColorSettingCard(
            cfg.themeColor,
            FIcon.PALETTE,
            '主题色',
            '调整你的应用主题颜色',
            self.aboutGroup
        )
        self.aboutCard = PrimaryPushSettingCard(
            '联系作者',
            FIcon.INFO,
            '当前版本:' + VERSION,
            '© Copyright' + f" {YEAR}, {AUTHOR}",
            self.aboutGroup
        )

        self.__init_widget()
        StyleSheet.SETTINGS.apply(self)

    def __init_widget(self):
        self.resize(500, 400)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 70, 0, 50)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

        # initialize layout
        self.__init_layout()
        self.__connect_signal_to_slot()

    def __init_layout(self):
        self.settingLabel.move(20, 20)
        # Removed personalization group and cards
        self.aboutGroup.addSettingCard(self.themeCard)
        self.aboutGroup.addSettingCard(self.themeColorCard)
        self.aboutGroup.addSettingCard(self.aboutCard)
        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(60, 0, 60, 0)
        # Removed personalGroup from layout
        self.expandLayout.addWidget(self.aboutGroup)
        self.scrollWidget.setObjectName('scrollWidget')
        self.settingLabel.setObjectName('settingLabel')

    def __show_restart_tooltip(self):
        """ show restart tooltip """
        InfoBar.warning(
            title='配置修改成功',
            content='修改会在重启软件后生效',
            orient=Qt.Orientation.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=1500,  # won't disappear automatically
            parent=self
        )

    # Removed __logout method and logoutCard signal connections

    def __connect_signal_to_slot(self):
        """ connect signal to slot """
        cfg.appRestartSig.connect(self.__show_restart_tooltip)
        cfg.themeChanged.connect(setTheme)
        self.themeColorCard.colorChanged.connect(setThemeColor)
        # Removed logoutCard and aboutCard signal connections
        self.aboutCard.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(FEEDBACK_URL)))