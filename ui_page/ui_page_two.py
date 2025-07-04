# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_two.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListView, QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import PrimaryPushButton

class Ui_page_two(object):
    def setupUi(self, page_two):
        if not page_two.objectName():
            page_two.setObjectName(u"page_two")
        page_two.resize(762, 582)
        self.horizontalLayout = QHBoxLayout(page_two)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftFrame = QFrame(page_two)
        self.leftFrame.setObjectName(u"leftFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftFrame.sizePolicy().hasHeightForWidth())
        self.leftFrame.setSizePolicy(sizePolicy)
        self.leftFrame.setMaximumSize(QSize(200, 16777215))
        self.leftContentLayout = QVBoxLayout(self.leftFrame)
        self.leftContentLayout.setObjectName(u"leftContentLayout")
        self.labelTitle = QLabel(self.leftFrame)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setStyleSheet(u"font-weight: bold; font-size: 14px;")

        self.leftContentLayout.addWidget(self.labelTitle)

        self.listView = QListView(self.leftFrame)
        self.listView.setObjectName(u"listView")

        self.leftContentLayout.addWidget(self.listView)

        self.pushButton = PrimaryPushButton(self.leftFrame)
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

        self.leftContentLayout.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.leftFrame)

        self.chartWidget = QFrame(page_two)
        self.chartWidget.setObjectName(u"chartWidget")
        self.chartLayout_2 = QVBoxLayout(self.chartWidget)
        self.chartLayout_2.setObjectName(u"chartLayout_2")
        self.chartLayout = QVBoxLayout()
        self.chartLayout.setObjectName(u"chartLayout")

        self.chartLayout_2.addLayout(self.chartLayout)


        self.horizontalLayout.addWidget(self.chartWidget)


        self.retranslateUi(page_two)

        self.pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(page_two)
    # setupUi

    def retranslateUi(self, page_two):
        page_two.setWindowTitle(QCoreApplication.translate("page_two", u"Form", None))
        self.labelTitle.setText(QCoreApplication.translate("page_two", u"\u9009\u62e9\u5b66\u751f", None))
        self.pushButton.setText(QCoreApplication.translate("page_two", u"\u5237\u65b0", None))
    # retranslateUi

