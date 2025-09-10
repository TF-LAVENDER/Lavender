# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page3.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Page3(object):
    def setupUi(self, Page3):
        if not Page3.objectName():
            Page3.setObjectName(u"Page3")
        Page3.resize(960, 400)
        Page3.setStyleSheet(u"background-color: #2d3242;")
        self.verticalLayout = QVBoxLayout(Page3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerWidget = QWidget(Page3)
        self.headerWidget.setObjectName(u"headerWidget")
        self.headerWidget.setMinimumSize(QSize(0, 40))
        self.headerWidget.setMaximumSize(QSize(16777215, 40))
        self.headerWidget.setStyleSheet(u"background-color: #272b4d;\n"
"color: white;")
        self.headerLayout = QHBoxLayout(self.headerWidget)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(20, 0, 20, 0)
        self.toggleWidget = QWidget(self.headerWidget)
        self.toggleWidget.setObjectName(u"toggleWidget")
        self.toggleWidget.setMinimumSize(QSize(200, 30))
        self.toggleWidget.setMaximumSize(QSize(200, 30))
        self.toggleWidget.setStyleSheet(u"background-color: #5056A5;\n"
"border-radius: 15px;")
        self.toggleLayout = QHBoxLayout(self.toggleWidget)
        self.toggleLayout.setSpacing(0)
        self.toggleLayout.setObjectName(u"toggleLayout")
        self.toggleLayout.setContentsMargins(0, 0, 0, 0)
        self.blockedButton = QPushButton(self.toggleWidget)
        self.blockedButton.setObjectName(u"blockedButton")
        self.blockedButton.setMinimumSize(QSize(100, 30))
        self.blockedButton.setMaximumSize(QSize(100, 30))
        self.blockedButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #ff4444;\n"
"    border-top-left-radius: 15px;\n"
"    border-bottom-left-radius: 15px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ff6666;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #cc3333;\n"
"}")
        self.blockedButton.setCheckable(True)
        self.blockedButton.setChecked(True)

        self.toggleLayout.addWidget(self.blockedButton)

        self.allowedButton = QPushButton(self.toggleWidget)
        self.allowedButton.setObjectName(u"allowedButton")
        self.allowedButton.setMinimumSize(QSize(100, 30))
        self.allowedButton.setMaximumSize(QSize(100, 30))
        self.allowedButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #5056A5;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #6066B5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4046A5;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #44ff44;\n"
"}")
        self.allowedButton.setCheckable(True)
        self.allowedButton.setChecked(False)

        self.toggleLayout.addWidget(self.allowedButton)


        self.headerLayout.addWidget(self.toggleWidget, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout.addWidget(self.headerWidget)

        self.tableWidget = QTableWidget(Page3)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"    gridline-color: rgb(50, 55, 100);\n"
"    background-color: rgb(45, 50, 95);\n"
"    alternate-background-color: rgb(68, 64, 122);\n"
"}\n"
"QTableWidget::item {\n"
"    padding: 5px;\n"
"    border-bottom: 1px solid rgb(50, 55, 100);\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgb(39, 43, 77);\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    font-weight: bold;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(70, 77, 140);\n"
"}")
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Page3)

        QMetaObject.connectSlotsByName(Page3)
    # setupUi

    def retranslateUi(self, Page3):
        Page3.setWindowTitle(QCoreApplication.translate("Page3", u"Security Log", None))
        self.blockedButton.setText(QCoreApplication.translate("Page3", u"\ud83d\udd34 Blocked", None))
        self.allowedButton.setText(QCoreApplication.translate("Page3", u"\ud83d\udfe2 Allowed", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Page3", u"ASC", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Page3", u"IP", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Page3", u"Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Page3", u"Description", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Page3", u"Description", None));
    # retranslateUi

