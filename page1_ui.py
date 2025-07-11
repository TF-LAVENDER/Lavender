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
        self.trafficContent.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.trafficContent)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.trafficContent)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.recv_send_ratio = QProgressBar(self.groupBox_2)
        self.recv_send_ratio.setObjectName(u"recv_send_ratio")
        self.recv_send_ratio.setEnabled(True)
        self.recv_send_ratio.setGeometry(QRect(110, 50, 131, 75))
        font = QFont()
        font.setPointSize(1)
        font.setWeight(QFont.Thin)
        self.recv_send_ratio.setFont(font)
        self.recv_send_ratio.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.recv_send_ratio.setStyleSheet(u"QProgressBar {\n"
"    border-radius: 37px;\n"
"    background-color: #ff5151;\n"
"    text-align: center;\n"
"    color: black;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #fff700;\n"
"    border-top-left-radius: 37px;\n"
"    border-bottom-left-radius: 37px;\n"
"}")
        self.recv_send_ratio.setMaximum(100)
        self.recv_send_ratio.setValue(45)
        self.recv_send_ratio.setTextVisible(False)
        self.recv_send_ratio.setInvertedAppearance(False)
        self.recv_kbs = QLabel(self.groupBox_2)
        self.recv_kbs.setObjectName(u"recv_kbs")
        self.recv_kbs.setGeometry(QRect(0, 80, 81, 20))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.recv_kbs.setFont(font1)
        self.recv_kbs.setStyleSheet(u"color: rgb(255, 255,255);")
        self.recv_kbs.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.send_kbs = QLabel(self.groupBox_2)
        self.send_kbs.setObjectName(u"send_kbs")
        self.send_kbs.setGeometry(QRect(270, 80, 71, 20))
        self.send_kbs.setFont(font1)
        self.send_kbs.setStyleSheet(u"color: rgb(255, 255,255);")
        self.send_kbs.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.line_2 = QFrame(self.groupBox_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setEnabled(False)
        self.line_2.setGeometry(QRect(80, -10, 187, 20))
        self.line_2.setStyleSheet(u"color: #a3a3a3;")
        self.line_2.setFrameShadow(QFrame.Shadow.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_3 = QFrame(self.groupBox_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(337, 42, 21, 100))
        self.line_3.setStyleSheet(u"color: #a3a3a3;")
        self.line_3.setFrameShadow(QFrame.Shadow.Plain)
        self.line_3.setFrameShape(QFrame.Shape.VLine)

        self.verticalLayout.addWidget(self.groupBox_2)


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
        self.WAN_BAR = QProgressBar(self.groupBox)
        self.WAN_BAR.setObjectName(u"WAN_BAR")
        self.WAN_BAR.setEnabled(True)
        self.WAN_BAR.setGeometry(QRect(90, 70, 345, 10))
        self.WAN_BAR.setFont(font)
        self.WAN_BAR.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.WAN_BAR.setStyleSheet(u"QProgressBar {\n"
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
        self.WAN_BAR.setMaximum(0)
        self.WAN_BAR.setValue(-1)
        self.WAN_BAR.setTextVisible(False)
        self.WAN_BAR.setInvertedAppearance(False)
        self.WAN = QLabel(self.groupBox)
        self.WAN.setObjectName(u"WAN")
        self.WAN.setGeometry(QRect(40, 66, 41, 16))
        self.WAN.setFont(font1)
        self.WAN.setStyleSheet(u"color: rgb(255, 255,255);")
        self.LAN = QLabel(self.groupBox)
        self.LAN.setObjectName(u"LAN")
        self.LAN.setGeometry(QRect(44, 96, 31, 16))
        self.LAN.setFont(font1)
        self.LAN.setStyleSheet(u"color: rgb(255, 255,255);")
        self.LAN_BAR = QProgressBar(self.groupBox)
        self.LAN_BAR.setObjectName(u"LAN_BAR")
        self.LAN_BAR.setGeometry(QRect(90, 100, 200, 10))
        self.LAN_BAR.setFont(font)
        self.LAN_BAR.setStyleSheet(u"QProgressBar {\n"
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
        self.LAN_BAR.setValue(45)
        self.LAN_BAR.setTextVisible(False)
        self.LAN_BAR.setInvertedAppearance(False)
        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setEnabled(False)
        self.line.setGeometry(QRect(130, -10, 293, 20))
        self.line.setStyleSheet(u"color: #a3a3a3;")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line_4 = QFrame(self.groupBox)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(-8, 42, 21, 100))
        self.line_4.setStyleSheet(u"color: #a3a3a3;")
        self.line_4.setFrameShadow(QFrame.Shadow.Plain)
        self.line_4.setFrameShape(QFrame.Shape.VLine)

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
        self.groupBox_2.setTitle("")
        self.recv_kbs.setText(QCoreApplication.translate("MainWindow", u"KB", None))
        self.send_kbs.setText(QCoreApplication.translate("MainWindow", u"KB", None))
        self.NetworkContent.setStyleSheet("")
        self.groupBox.setTitle("")
        self.WAN.setText(QCoreApplication.translate("MainWindow", u"WAN", None))
        self.LAN.setText(QCoreApplication.translate("MainWindow", u"LAN", None))
    # retranslateUi

