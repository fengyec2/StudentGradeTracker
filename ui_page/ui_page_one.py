# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_one.ui'
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
    QLabel, QListView, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

from qfluentwidgets import PrimaryPushButton

class Ui_page_one(object):
    def setupUi(self, page_one):
        if not page_one.objectName():
            page_one.setObjectName(u"page_one")
        page_one.resize(762, 582)
        self.horizontalLayout = QHBoxLayout(page_one)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftPanel = QFrame(page_one)
        self.leftPanel.setObjectName(u"leftPanel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftPanel.sizePolicy().hasHeightForWidth())
        self.leftPanel.setSizePolicy(sizePolicy)
        self.leftPanel.setMaximumSize(QSize(300, 16777215))
        self.leftPanel.setStyleSheet(u"\n"
"        background-color: white;\n"
"        border-radius: 8px;\n"
"        padding: 10px;\n"
"      ")
        self.leftLayout = QVBoxLayout(self.leftPanel)
        self.leftLayout.setObjectName(u"leftLayout")
        self.labelExamList = QLabel(self.leftPanel)
        self.labelExamList.setObjectName(u"labelExamList")
        self.labelExamList.setStyleSheet(u"font-weight: bold; font-size: 14px;")

        self.leftLayout.addWidget(self.labelExamList)

        self.listView = QListView(self.leftPanel)
        self.listView.setObjectName(u"listView")
        self.listView.setStyleSheet(u"\n"
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

        self.leftLayout.addWidget(self.listView)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.pushButton = PrimaryPushButton(self.leftPanel)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(0, 38))

        self.buttonLayout.addWidget(self.pushButton)

        self.btnDelete = QPushButton(self.leftPanel)
        self.btnDelete.setObjectName(u"btnDelete")
        sizePolicy1.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy1)
        self.btnDelete.setMinimumSize(QSize(0, 38))
        self.btnDelete.setStyleSheet(u"\n"
"             QPushButton {\n"
"               color: #ff4d4f;\n"
"               border: 1px solid #ffccc7;\n"
"             }\n"
"             QPushButton:hover {\n"
"               background-color: #fff2f0;\n"
"             }\n"
"           ")

        self.buttonLayout.addWidget(self.btnDelete)


        self.leftLayout.addLayout(self.buttonLayout)


        self.horizontalLayout.addWidget(self.leftPanel)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.upperRightPanel = QFrame(page_one)
        self.upperRightPanel.setObjectName(u"upperRightPanel")
        self.upperRightPanel.setStyleSheet(u"\n"
"        background-color: white;\n"
"        border-radius: 8px;\n"
"        padding: 10px;\n"
"      ")
        self.rightLayout_2 = QVBoxLayout(self.upperRightPanel)
        self.rightLayout_2.setObjectName(u"rightLayout_2")
        self.labelPreview_2 = QLabel(self.upperRightPanel)
        self.labelPreview_2.setObjectName(u"labelPreview_2")
        self.labelPreview_2.setStyleSheet(u"font-weight: bold; font-size: 14px;")

        self.rightLayout_2.addWidget(self.labelPreview_2)

        self.examNameLayout = QHBoxLayout()
        self.examNameLayout.setObjectName(u"examNameLayout")
        self.labelExamName = QLabel(self.upperRightPanel)
        self.labelExamName.setObjectName(u"labelExamName")

        self.examNameLayout.addWidget(self.labelExamName)

        self.btnEditExamName = QPushButton(self.upperRightPanel)
        self.btnEditExamName.setObjectName(u"btnEditExamName")

        self.examNameLayout.addWidget(self.btnEditExamName)


        self.rightLayout_2.addLayout(self.examNameLayout)

        self.examDateLayout = QHBoxLayout()
        self.examDateLayout.setObjectName(u"examDateLayout")
        self.labelExamDate = QLabel(self.upperRightPanel)
        self.labelExamDate.setObjectName(u"labelExamDate")

        self.examDateLayout.addWidget(self.labelExamDate)

        self.btnEditExamDate = QPushButton(self.upperRightPanel)
        self.btnEditExamDate.setObjectName(u"btnEditExamDate")

        self.examDateLayout.addWidget(self.btnEditExamDate)


        self.rightLayout_2.addLayout(self.examDateLayout)


        self.verticalLayout.addWidget(self.upperRightPanel)

        self.rightPanel = QFrame(page_one)
        self.rightPanel.setObjectName(u"rightPanel")
        self.rightPanel.setStyleSheet(u"\n"
"        background-color: white;\n"
"        border-radius: 8px;\n"
"        padding: 10px;\n"
"      ")
        self.rightLayout = QVBoxLayout(self.rightPanel)
        self.rightLayout.setObjectName(u"rightLayout")
        self.labelPreview = QLabel(self.rightPanel)
        self.labelPreview.setObjectName(u"labelPreview")
        self.labelPreview.setStyleSheet(u"font-weight: bold; font-size: 14px;")

        self.rightLayout.addWidget(self.labelPreview)

        self.tableView = QTableView(self.rightPanel)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"\n"
"           QTableView {\n"
"             border: 1px solid #ddd;\n"
"             border-radius: 4px;\n"
"             gridline-color: #f0f0f0;\n"
"           }\n"
"           QHeaderView::section {\n"
"             background-color: #f7f7f7;\n"
"             padding: 5px;\n"
"             border: none;\n"
"             min-height: 40px;  /* \u663e\u5f0f\u8bbe\u7f6e\u9ad8\u5ea6 */\n"
"             min-width: 40px;  /* \u663e\u5f0f\u8bbe\u7f6e\u5bbd\u5ea6 */\n"
"           }\n"
"         ")
        self.tableView.setAlternatingRowColors(True)

        self.rightLayout.addWidget(self.tableView)


        self.verticalLayout.addWidget(self.rightPanel)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(page_one)

        QMetaObject.connectSlotsByName(page_one)
    # setupUi

    def retranslateUi(self, page_one):
        page_one.setWindowTitle(QCoreApplication.translate("page_one", u"Form", None))
        self.labelExamList.setText(QCoreApplication.translate("page_one", u"\u5df2\u5bfc\u5165\u7684\u8003\u8bd5", None))
        self.pushButton.setText(QCoreApplication.translate("page_one", u"\u5bfc\u5165\u65b0\u8003\u8bd5", None))
        self.btnDelete.setText(QCoreApplication.translate("page_one", u"\u5220\u9664", None))
        self.labelPreview_2.setText(QCoreApplication.translate("page_one", u"\u8003\u8bd5\u4fe1\u606f", None))
        self.labelExamName.setText(QCoreApplication.translate("page_one", u"\u8bf7\u9009\u62e9\u8003\u8bd5", None))
        self.btnEditExamName.setText(QCoreApplication.translate("page_one", u"\u4fee\u6539", None))
        self.labelExamDate.setText(QCoreApplication.translate("page_one", u"\u8bf7\u9009\u62e9\u8003\u8bd5", None))
        self.btnEditExamDate.setText(QCoreApplication.translate("page_one", u"\u4fee\u6539", None))
        self.labelPreview.setText(QCoreApplication.translate("page_one", u"\u6570\u636e\u9884\u89c8 (\u51710\u884c)", None))
    # retranslateUi

