# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_top_in_class.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListView, QSizePolicy,
    QWidget)

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
        self.leftPanel.setStyleSheet(u"\n"
"        background-color: white;\n"
"        border-radius: 8px;\n"
"        padding: 10px;\n"
"      ")
        self.gridLayout = QGridLayout(self.leftPanel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelExamList = QLabel(self.leftPanel)
        self.labelExamList.setObjectName(u"labelExamList")
        self.labelExamList.setStyleSheet(u"font-weight: bold; font-size: 14px;")

        self.gridLayout.addWidget(self.labelExamList, 0, 0, 1, 1)

        self.examListView = QListView(self.leftPanel)
        self.examListView.setObjectName(u"examListView")
        self.examListView.setStyleSheet(u"\n"
"           QListView {\n"
"             border: 1px solid #dcdfe6;\n"
"             border-radius: 4px;\n"
"             padding: 4px;\n"
"             background-color: #ffffff;\n"
"           }\n"
"           QListView::item {\n"
"             padding: 8px 12px;\n"
"             border-bottom: 1px solid #ebeef5;\n"
"           }\n"
"           QListView::item:hover {\n"
"             background-color: #f5f7fa;\n"
"           }\n"
"           QListView::item:selected {\n"
"             background-color: #ecf5ff;\n"
"             color: #409eff;\n"
"             border-left: 3px solid #409eff;\n"
"           }\n"
"         ")

        self.gridLayout.addWidget(self.examListView, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.leftPanel)

        self.rightPanel = QFrame(page_top_in_class)
        self.rightPanel.setObjectName(u"rightPanel")
        self.rightPanel.setStyleSheet(u"\n"
"        background-color: white;\n"
"        border-radius: 8px;\n"
"        padding: 10px;\n"
"      ")
        self.labelChartTitle = QLabel(self.rightPanel)
        self.labelChartTitle.setObjectName(u"labelChartTitle")
        self.labelChartTitle.setGeometry(QRect(19, 91, 140, 38))
        self.labelChartTitle.setStyleSheet(u"font-weight: bold; font-size: 14px;")
        self.chartWidget = QWidget(self.rightPanel)
        self.chartWidget.setObjectName(u"chartWidget")
        self.chartWidget.setGeometry(QRect(19, 163, 458, 400))
        self.chartWidget.setMinimumSize(QSize(0, 400))
        self.classComboBox = QComboBox(self.rightPanel)
        self.classComboBox.setObjectName(u"classComboBox")
        self.classComboBox.setGeometry(QRect(220, 20, 80, 38))
        self.labelClass = QLabel(self.rightPanel)
        self.labelClass.setObjectName(u"labelClass")
        self.labelClass.setGeometry(QRect(20, 20, 86, 36))

        self.horizontalLayout.addWidget(self.rightPanel)


        self.retranslateUi(page_top_in_class)

        QMetaObject.connectSlotsByName(page_top_in_class)
    # setupUi

    def retranslateUi(self, page_top_in_class):
        page_top_in_class.setWindowTitle(QCoreApplication.translate("page_top_in_class", u"\u73ed\u7ea7\u5355\u79d1\u738b\u8868\u73b0", None))
        self.labelExamList.setText(QCoreApplication.translate("page_top_in_class", u"\u9009\u62e9\u8003\u8bd5", None))
        self.labelChartTitle.setText(QCoreApplication.translate("page_top_in_class", u"\u73ed\u7ea7\u5355\u79d1\u738b\u5bf9\u6bd4\u56fe", None))
        self.labelClass.setText(QCoreApplication.translate("page_top_in_class", u"\u9009\u62e9\u73ed\u7ea7\uff1a", None))
    # retranslateUi

