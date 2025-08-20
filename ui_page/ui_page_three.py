# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_three.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QListView, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

from qfluentwidgets import PrimaryPushButton

class Ui_page_three(object):
    def setupUi(self, page_three):
        if not page_three.objectName():
            page_three.setObjectName(u"page_three")
        page_three.resize(762, 582)
        self.horizontalLayout = QHBoxLayout(page_three)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftFrame = QFrame(page_three)
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

        self.rightFrame = QFrame(page_three)
        self.rightFrame.setObjectName(u"rightFrame")
        self.chartLayout_2 = QVBoxLayout(self.rightFrame)
        self.chartLayout_2.setObjectName(u"chartLayout_2")
        self.tableView = QTableView(self.rightFrame)
        self.tableView.setObjectName(u"tableView")

        self.chartLayout_2.addWidget(self.tableView)


        self.horizontalLayout.addWidget(self.rightFrame)


        self.retranslateUi(page_three)

        self.pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(page_three)
    # setupUi

    def retranslateUi(self, page_three):
        page_three.setWindowTitle(QCoreApplication.translate("page_three", u"Form", None))
        self.labelTitle.setText(QCoreApplication.translate("page_three", u"\u9009\u62e9\u5b66\u751f", None))
        self.pushButton.setText(QCoreApplication.translate("page_three", u"\u5237\u65b0", None))
    # retranslateUi

