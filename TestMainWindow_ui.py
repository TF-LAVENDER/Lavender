# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestMainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(437, 470)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 70, 50, 16))
        self.textEdit1 = QTextEdit(self.centralwidget)
        self.textEdit1.setObjectName(u"textEdit1")
        self.textEdit1.setGeometry(QRect(80, 100, 301, 161))
        self.pushButton1 = QPushButton(self.centralwidget)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setGeometry(QRect(90, 280, 75, 24))
        self.pushButton2 = QPushButton(self.centralwidget)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setGeometry(QRect(90, 320, 75, 24))
        self.pushButton3 = QPushButton(self.centralwidget)
        self.pushButton3.setObjectName(u"pushButton3")
        self.pushButton3.setGeometry(QRect(90, 360, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 437, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

