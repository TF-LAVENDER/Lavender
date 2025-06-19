# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page1.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 960, 500))
        self.widget.setStyleSheet(u"# border-image:url(\"images/page1.png\")")
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-10, -10, 980, 320))
        self.chartContainer = QVBoxLayout(self.verticalLayoutWidget)
        self.chartContainer.setSpacing(0)
        self.chartContainer.setObjectName(u"chartContainer")
        self.chartContainer.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_2 = QWidget(self.widget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 300, 374, 200))
        self.trafficContainer = QVBoxLayout(self.verticalLayoutWidget_2)
        self.trafficContainer.setSpacing(0)
        self.trafficContainer.setObjectName(u"trafficContainer")
        self.trafficContainer.setContentsMargins(0, 0, 0, 0)
        self.trafficContent = QFrame(self.verticalLayoutWidget_2)
        self.trafficContent.setObjectName(u"trafficContent")
        self.trafficContent.setStyleSheet(u"border-image:url(\"images/image1.png\")")
        self.verticalLayout = QVBoxLayout(self.trafficContent)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.trafficContainer.addWidget(self.trafficContent)

        self.verticalLayoutWidget_3 = QWidget(self.widget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(374, 300, 586, 200))
        self.NetworkContainer = QVBoxLayout(self.verticalLayoutWidget_3)
        self.NetworkContainer.setSpacing(0)
        self.NetworkContainer.setObjectName(u"NetworkContainer")
        self.NetworkContainer.setContentsMargins(0, 0, 0, 0)
        self.NetworkContent = QFrame(self.verticalLayoutWidget_3)
        self.NetworkContent.setObjectName(u"NetworkContent")
        self.NetworkContent.setStyleSheet(u"border-image:url(\"images/image2.png\")")
        self.verticalLayout_2 = QVBoxLayout(self.NetworkContent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.NetworkContainer.addWidget(self.NetworkContent)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 960, 36))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

