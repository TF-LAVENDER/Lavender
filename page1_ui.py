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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QMainWindow, QMenuBar, QProgressBar, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(937, 500)
        MainWindow.setAcceptDrops(False)
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
        self.verticalLayout_2 = QVBoxLayout(self.NetworkContent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.NetworkContent)
        self.groupBox.setObjectName(u"groupBox")
        self.WAN = QProgressBar(self.groupBox)
        self.WAN.setObjectName(u"WAN")
        self.WAN.setEnabled(True)
        self.WAN.setGeometry(QRect(90, 70, 345, 10))
        font = QFont()
        font.setPointSize(1)
        font.setWeight(QFont.Thin)
        self.WAN.setFont(font)
        self.WAN.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.WAN.setStyleSheet(u"QProgressBar {\n"
"    border-radius: 5px;\n"
"    background-color: #ff5151;\n"
"    text-align: center;\n"
"    color: black;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #fff700;\n"
"    border-top-left-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"}")
        self.WAN.setMaximum(0)
        self.WAN.setValue(-1)
        self.WAN.setTextVisible(False)
        self.WAN.setInvertedAppearance(False)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 66, 41, 16))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255,255);")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(44, 96, 31, 16))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255,255);")
        self.LAN = QProgressBar(self.groupBox)
        self.LAN.setObjectName(u"LAN")
        self.LAN.setGeometry(QRect(90, 100, 200, 10))
        self.LAN.setFont(font)
        self.LAN.setStyleSheet(u"QProgressBar {\n"
"    border-radius: 5px;\n"
"    background-color: #ff5151;\n"
"    text-align: center;\n"
"    color: black;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #fff700;\n"
"    border-top-left-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"}")
        self.LAN.setValue(45)
        self.LAN.setTextVisible(False)
        self.LAN.setInvertedAppearance(False)
        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setEnabled(False)
        self.line.setGeometry(QRect(130, -10, 293, 20))
        self.line.setStyleSheet(u"color: #a3a3a3;")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_2.addWidget(self.groupBox)


        self.NetworkContainer.addWidget(self.NetworkContent)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 937, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.NetworkContent.setStyleSheet("")
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"WAN", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LAN", None))
    # retranslateUi

