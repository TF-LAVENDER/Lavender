# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 545)
        MainWindow.setStyleSheet(u"background-color: rgb(35, 35, 35); ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.menuButton1 = QPushButton(self.centralwidget)
        self.menuButton1.setObjectName(u"menuButton1")
        self.menuButton1.setGeometry(QRect(240, 7, 120, 30))
        self.menuButton1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.menuButton1.setStyleSheet(u"border-image:url(\"images/menu1_on.png\")")
        self.menuButton2 = QPushButton(self.centralwidget)
        self.menuButton2.setObjectName(u"menuButton2")
        self.menuButton2.setGeometry(QRect(360, 7, 120, 30))
        self.menuButton2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.menuButton2.setStyleSheet(u"border-image:url(\"images/menu2_off.png\")")
        self.menuButton3 = QPushButton(self.centralwidget)
        self.menuButton3.setObjectName(u"menuButton3")
        self.menuButton3.setGeometry(QRect(480, 7, 120, 30))
        self.menuButton3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.menuButton3.setStyleSheet(u"border-image:url(\"images/menu3_off.png\")")
        self.menuButton4 = QPushButton(self.centralwidget)
        self.menuButton4.setObjectName(u"menuButton4")
        self.menuButton4.setGeometry(QRect(600, 7, 120, 30))
        self.menuButton4.setStyleSheet(u"border-image:url(\"images/menu4_off.png\")")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 45, 960, 545))
        self.contentArea = QHBoxLayout(self.horizontalLayoutWidget)
        self.contentArea.setSpacing(0)
        self.contentArea.setObjectName(u"contentArea")
        self.contentArea.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.contentArea.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.horizontalLayoutWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(False)

        self.contentArea.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 960, 36))
        self.menubar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton1.setText("")
        self.menuButton2.setText("")
        self.menuButton3.setText("")
        self.menuButton4.setText("")
    # retranslateUi

