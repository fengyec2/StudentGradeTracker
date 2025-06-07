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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QListView,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

from qfluentwidgets import PrimaryPushButton

class Ui_page_three(object):
    def setupUi(self, page_three):
        if not page_three.objectName():
            page_three.setObjectName(u"page_three")
        page_three.resize(762, 582)
        self.horizontalLayoutWidget = QWidget(page_three)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(50, 70, 631, 351))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listView = QListView(self.horizontalLayoutWidget)
        self.listView.setObjectName(u"listView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.listView)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = PrimaryPushButton(self.horizontalLayoutWidget)
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

        self.verticalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.tableView = QTableView(self.horizontalLayoutWidget)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout.addWidget(self.tableView)


        self.retranslateUi(page_three)

        self.pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(page_three)
    # setupUi

    def retranslateUi(self, page_three):
        page_three.setWindowTitle(QCoreApplication.translate("page_three", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("page_three", u"\u5237\u65b0", None))
    # retranslateUi

