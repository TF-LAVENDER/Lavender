# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page2.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_Page3(object):
    def setupUi(self, Page3):
        if not Page3.objectName():
            Page3.setObjectName(u"Page3")
        Page3.resize(960, 500)
        Page3.setStyleSheet(u"background-color: #2d3242;")
        self.verticalLayout = QVBoxLayout(Page3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerWidget = QWidget(Page3)
        self.headerWidget.setObjectName(u"headerWidget")
        self.headerWidget.setMinimumSize(QSize(0, 40))
        self.headerWidget.setMaximumSize(QSize(16777215, 40))
        self.headerWidget.setStyleSheet(u"margin: 0;\n"
"padding: 0;\n"
"color: white;")
        self.blockedButton = QPushButton(self.headerWidget)
        self.blockedButton.setObjectName(u"blockedButton")
        self.blockedButton.setGeometry(QRect(0, 0, 100, 40))
        self.blockedButton.setMinimumSize(QSize(100, 40))
        self.blockedButton.setMaximumSize(QSize(100, 40))
        self.blockedButton.setStyleSheet(u"border-image: url(\"components/page2/images/blocked_on.png\");\n"
"margin: 0;")
        self.blockedButton.setCheckable(True)
        self.blockedButton.setChecked(True)
        self.allowedButton = QPushButton(self.headerWidget)
        self.allowedButton.setObjectName(u"allowedButton")
        self.allowedButton.setGeometry(QRect(101, 0, 100, 40))
        self.allowedButton.setMinimumSize(QSize(100, 40))
        self.allowedButton.setMaximumSize(QSize(100, 40))
        self.allowedButton.setStyleSheet(u"border-image: url(\"components/page2/images/allowed_off.png\");\n"
"margin: 0;")
        self.allowedButton.setCheckable(True)
        self.allowedButton.setChecked(False)
        self.addButton = QPushButton(self.headerWidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(870, 0, 75, 24))

        self.verticalLayout.addWidget(self.headerWidget)

        self.blockedTableView = QTableView(Page3)
        self.blockedTableView.setObjectName(u"blockedTableView")
        self.blockedTableView.setStyleSheet(u"QTableView {\n"
"    gridline-color: rgb(50, 55, 100);\n"
"    alternate-background-color: rgb(68, 64, 122);\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	border: 0;\n"
"}\n"
"QTableView::item {\n"
"    padding: 5px;\n"
"    border-bottom: 1px solid rgb(68, 64, 122);\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgb(68, 64, 122);\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    font-weight: bold;\n"
"}\n"
"QTableView::item:selected {\n"
"    background-color: rgb(70, 77, 140);\n"
"}")

        self.verticalLayout.addWidget(self.blockedTableView)


        self.retranslateUi(Page3)

        QMetaObject.connectSlotsByName(Page3)
    # setupUi

    def retranslateUi(self, Page3):
        Page3.setWindowTitle(QCoreApplication.translate("Page3", u"IP List", None))
        self.blockedButton.setText("")
        self.allowedButton.setText("")
        self.addButton.setText(QCoreApplication.translate("Page3", u"PushButton", None))
    # retranslateUi

