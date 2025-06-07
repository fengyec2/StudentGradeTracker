# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_class_grade.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_page_class_grade(object):
    def setupUi(self, page_class_grade):
        if not page_class_grade.objectName():
            page_class_grade.setObjectName(u"page_class_grade")
        page_class_grade.resize(800, 600)
        self.verticalLayout_4 = QVBoxLayout(page_class_grade)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.statusbar = QStatusBar(page_class_grade)
        self.statusbar.setObjectName(u"statusbar")

        self.verticalLayout_4.addWidget(self.statusbar)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(page_class_grade)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboExam = QComboBox(page_class_grade)
        self.comboExam.setObjectName(u"comboExam")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboExam.sizePolicy().hasHeightForWidth())
        self.comboExam.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.comboExam)

        self.label_2 = QLabel(page_class_grade)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.listClasses = QListWidget(page_class_grade)
        self.listClasses.setObjectName(u"listClasses")
        self.listClasses.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.horizontalLayout.addWidget(self.listClasses)

        self.btnQuery = QPushButton(page_class_grade)
        self.btnQuery.setObjectName(u"btnQuery")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnQuery.sizePolicy().hasHeightForWidth())
        self.btnQuery.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.btnQuery)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(page_class_grade)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setMinimumSize(QSize(0, 400))
        self.tabTable = QWidget()
        self.tabTable.setObjectName(u"tabTable")
        self.verticalLayout_2 = QVBoxLayout(self.tabTable)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableScores = QTableWidget(self.tabTable)
        if (self.tableScores.columnCount() < 5):
            self.tableScores.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableScores.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableScores.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableScores.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableScores.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableScores.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableScores.setObjectName(u"tableScores")
        self.tableScores.setRowCount(0)
        self.tableScores.setColumnCount(5)

        self.verticalLayout_2.addWidget(self.tableScores)

        self.tabWidget.addTab(self.tabTable, "")
        self.tabChart = QWidget()
        self.tabChart.setObjectName(u"tabChart")
        self.verticalLayout_3 = QVBoxLayout(self.tabChart)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widgetChart = QWidget(self.tabChart)
        self.widgetChart.setObjectName(u"widgetChart")
        self.widgetChart.setStyleSheet(u"background-color: #f0f0f0;")

        self.verticalLayout_3.addWidget(self.widgetChart)

        self.tabWidget.addTab(self.tabChart, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelStats = QLabel(page_class_grade)
        self.labelStats.setObjectName(u"labelStats")

        self.horizontalLayout_2.addWidget(self.labelStats)

        self.editNotes = QLineEdit(page_class_grade)
        self.editNotes.setObjectName(u"editNotes")

        self.horizontalLayout_2.addWidget(self.editNotes)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.retranslateUi(page_class_grade)

        QMetaObject.connectSlotsByName(page_class_grade)
    # setupUi

    def retranslateUi(self, page_class_grade):
        page_class_grade.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("page_class_grade", u"\u9009\u62e9\u8003\u8bd5\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("page_class_grade", u"\u9009\u62e9\u73ed\u7ea7\uff1a", None))
        self.btnQuery.setText(QCoreApplication.translate("page_class_grade", u"\u67e5\u8be2", None))
        ___qtablewidgetitem = self.tableScores.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("page_class_grade", u"\u73ed\u7ea7", None));
        ___qtablewidgetitem1 = self.tableScores.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("page_class_grade", u"\u8bed\u6587", None));
        ___qtablewidgetitem2 = self.tableScores.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("page_class_grade", u"\u6570\u5b66", None));
        ___qtablewidgetitem3 = self.tableScores.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("page_class_grade", u"\u82f1\u8bed", None));
        ___qtablewidgetitem4 = self.tableScores.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("page_class_grade", u"\u5e73\u5747\u5206", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTable), QCoreApplication.translate("page_class_grade", u"\u8868\u683c\u89c6\u56fe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabChart), QCoreApplication.translate("page_class_grade", u"\u56fe\u8868\u89c6\u56fe", None))
        self.labelStats.setText(QCoreApplication.translate("page_class_grade", u"\u5e74\u7ea7\u5e73\u5747\u5206\uff1a--", None))
        self.editNotes.setPlaceholderText(QCoreApplication.translate("page_class_grade", u"\u8f93\u5165\u5907\u6ce8...", None))
    # retranslateUi

