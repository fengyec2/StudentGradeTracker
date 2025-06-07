# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_two.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListView, QSizePolicy,
    QVBoxLayout, QWidget)

from qfluentwidgets import PrimaryPushButton

class Ui_page_two(object):
    def setupUi(self, page_two):
        if not page_two.objectName():
            page_two.setObjectName(u"page_two")
        page_two.resize(762, 582)
        self.horizontalLayout = QHBoxLayout(page_two)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listView = QListView(page_two)
        self.listView.setObjectName(u"listView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.listView)

        self.pushButton = PrimaryPushButton(page_two)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(0, 35))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        self.pushButton.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton)

        self.chartWidget = QWidget(page_two)
        self.chartWidget.setObjectName(u"chartWidget")
        self.chartLayout = QVBoxLayout(self.chartWidget)
        self.chartLayout.setObjectName(u"chartLayout")
        self.chartLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.chartWidget)


        self.retranslateUi(page_two)

        self.pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(page_two)
    # setupUi

    def retranslateUi(self, page_two):
        page_two.setWindowTitle(QCoreApplication.translate("page_two", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("page_two", u"\u5237\u65b0", None))
    # retranslateUi

