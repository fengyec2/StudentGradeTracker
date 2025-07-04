# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_class_grade.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import PrimaryPushButton

class Ui_page_class_grade(object):
    def setupUi(self, page_class_grade):
        if not page_class_grade.objectName():
            page_class_grade.setObjectName(u"page_class_grade")
        page_class_grade.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(page_class_grade.sizePolicy().hasHeightForWidth())
        page_class_grade.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(page_class_grade)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frameQueryCard = QFrame(page_class_grade)
        self.frameQueryCard.setObjectName(u"frameQueryCard")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameQueryCard.sizePolicy().hasHeightForWidth())
        self.frameQueryCard.setSizePolicy(sizePolicy1)
        self.frameQueryCard.setMaximumSize(QSize(16777215, 100))
        self.frameQueryCard.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.frameQueryCard)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnRefresh = QPushButton(self.frameQueryCard)
        self.btnRefresh.setObjectName(u"btnRefresh")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnRefresh.sizePolicy().hasHeightForWidth())
        self.btnRefresh.setSizePolicy(sizePolicy2)
        self.btnRefresh.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.btnRefresh)

        self.label = QLabel(self.frameQueryCard)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.label)

        self.comboExam = QComboBox(self.frameQueryCard)
        self.comboExam.setObjectName(u"comboExam")
        self.comboExam.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.comboExam)

        self.label_2 = QLabel(self.frameQueryCard)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.listClasses = QListWidget(self.frameQueryCard)
        self.listClasses.setObjectName(u"listClasses")
        self.listClasses.setMinimumSize(QSize(100, 0))
        self.listClasses.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.horizontalLayout.addWidget(self.listClasses)

        self.btnQuery = PrimaryPushButton(self.frameQueryCard)
        self.btnQuery.setObjectName(u"btnQuery")
        sizePolicy2.setHeightForWidth(self.btnQuery.sizePolicy().hasHeightForWidth())
        self.btnQuery.setSizePolicy(sizePolicy2)
        self.btnQuery.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.btnQuery)


        self.verticalLayout.addWidget(self.frameQueryCard)

        self.frameResultCard = QFrame(page_class_grade)
        self.frameResultCard.setObjectName(u"frameResultCard")
        self.frameResultCard.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.frameResultCard)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.frameResultCard)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 400))
        self.tabTable_2 = QWidget()
        self.tabTable_2.setObjectName(u"tabTable_2")
        self.verticalLayout_table_2 = QVBoxLayout(self.tabTable_2)
        self.verticalLayout_table_2.setObjectName(u"verticalLayout_table_2")
        self.tableScores = QTableWidget(self.tabTable_2)
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

        self.verticalLayout_table_2.addWidget(self.tableScores)

        self.tabWidget.addTab(self.tabTable_2, "")
        self.tabChart_2 = QWidget()
        self.tabChart_2.setObjectName(u"tabChart_2")
        self.verticalLayout_4 = QVBoxLayout(self.tabChart_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widgetChart = QWidget(self.tabChart_2)
        self.widgetChart.setObjectName(u"widgetChart")

        self.verticalLayout_4.addWidget(self.widgetChart)

        self.tabWidget.addTab(self.tabChart_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frameResultCard)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelStats = QLabel(page_class_grade)
        self.labelStats.setObjectName(u"labelStats")

        self.horizontalLayout_2.addWidget(self.labelStats)

        self.editNotes = QLineEdit(page_class_grade)
        self.editNotes.setObjectName(u"editNotes")

        self.horizontalLayout_2.addWidget(self.editNotes)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(page_class_grade)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(page_class_grade)
    # setupUi

    def retranslateUi(self, page_class_grade):
        page_class_grade.setWindowTitle("")
        self.btnRefresh.setText(QCoreApplication.translate("page_class_grade", u"\u5237\u65b0", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTable_2), QCoreApplication.translate("page_class_grade", u"\u8868\u683c\u89c6\u56fe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabChart_2), QCoreApplication.translate("page_class_grade", u"\u56fe\u8868\u89c6\u56fe", None))
        self.labelStats.setText(QCoreApplication.translate("page_class_grade", u"\u5e74\u7ea7\u5e73\u5747\u5206\uff1a--", None))
        self.editNotes.setPlaceholderText(QCoreApplication.translate("page_class_grade", u"\u8f93\u5165\u5907\u6ce8...", None))
    # retranslateUi

