# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_top_in_class.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListView, QSizePolicy,
    QVBoxLayout, QWidget)

from qfluentwidgets import PrimaryPushButton

class Ui_page_top_in_class(object):
    def setupUi(self, page_top_in_class):
        if not page_top_in_class.objectName():
            page_top_in_class.setObjectName(u"page_top_in_class")
        page_top_in_class.resize(800, 600)
        self.horizontalLayout = QHBoxLayout(page_top_in_class)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftPanel = QFrame(page_top_in_class)
        self.leftPanel.setObjectName(u"leftPanel")
        self.leftPanel.setMaximumSize(QSize(280, 16777215))
        self.gridLayout = QGridLayout(self.leftPanel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelExamList = QLabel(self.leftPanel)
        self.labelExamList.setObjectName(u"labelExamList")
        self.labelExamList.setStyleSheet(u"font-weight: bold; font-size: 14px;")

        self.verticalLayout_2.addWidget(self.labelExamList)

        self.listView = QListView(self.leftPanel)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_2.addWidget(self.listView)

        self.pushButton = PrimaryPushButton(self.leftPanel)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(0, 35))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        self.pushButton.setFont(font)

        self.verticalLayout_2.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.leftPanel)

        self.rightPanel = QFrame(page_top_in_class)
        self.rightPanel.setObjectName(u"rightPanel")
        self.gridLayout_2 = QGridLayout(self.rightPanel)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelClass = QLabel(self.rightPanel)
        self.labelClass.setObjectName(u"labelClass")

        self.horizontalLayout_2.addWidget(self.labelClass)

        self.comboBoxClass = QComboBox(self.rightPanel)
        self.comboBoxClass.setObjectName(u"comboBoxClass")

        self.horizontalLayout_2.addWidget(self.comboBoxClass)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.labelChartTitle = QLabel(self.rightPanel)
        self.labelChartTitle.setObjectName(u"labelChartTitle")
        self.labelChartTitle.setStyleSheet(u"font-weight: bold; font-size: 14px;")

        self.verticalLayout.addWidget(self.labelChartTitle)

        self.widgetChart = QWidget(self.rightPanel)
        self.widgetChart.setObjectName(u"widgetChart")
        self.widgetChart.setMinimumSize(QSize(0, 400))

        self.verticalLayout.addWidget(self.widgetChart)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.rightPanel)


        self.retranslateUi(page_top_in_class)

        self.pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(page_top_in_class)
    # setupUi

    def retranslateUi(self, page_top_in_class):
        page_top_in_class.setWindowTitle(QCoreApplication.translate("page_top_in_class", u"\u73ed\u7ea7\u5355\u79d1\u738b\u8868\u73b0", None))
        self.labelExamList.setText(QCoreApplication.translate("page_top_in_class", u"\u9009\u62e9\u8003\u8bd5", None))
        self.pushButton.setText(QCoreApplication.translate("page_top_in_class", u"\u5237\u65b0", None))
        self.labelClass.setText(QCoreApplication.translate("page_top_in_class", u"\u9009\u62e9\u73ed\u7ea7\uff1a", None))
        self.labelChartTitle.setText(QCoreApplication.translate("page_top_in_class", u"\u73ed\u7ea7\u5355\u79d1\u738b\u5bf9\u6bd4\u56fe", None))
    # retranslateUi

