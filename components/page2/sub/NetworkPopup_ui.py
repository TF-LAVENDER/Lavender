# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NetworkPopup.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_NetworkPopup(object):
    def setupUi(self, NetworkPopup):
        if not NetworkPopup.objectName():
            NetworkPopup.setObjectName(u"NetworkPopup")
        NetworkPopup.resize(500, 200)
        NetworkPopup.setStyleSheet(u"background-color: #232323;")
        self.protocolLabel = QLabel(NetworkPopup)
        self.protocolLabel.setObjectName(u"protocolLabel")
        self.protocolLabel.setGeometry(QRect(20, 10, 65, 16))
        self.protocolLabel.setStyleSheet(u"")
        self.protocolLane = QLineEdit(NetworkPopup)
        self.protocolLane.setObjectName(u"protocolLane")
        self.protocolLane.setGeometry(QRect(20, 30, 120, 30))
        self.protocolLane.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;\n"
"")
        self.cancelButton = QPushButton(NetworkPopup)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(280, 150, 100, 40))
        self.cancelButton.setStyleSheet(u"border-image: url(\"components/page2/sub/images/2.png\");\n"
"margin: 0;")
        self.confirmButton = QPushButton(NetworkPopup)
        self.confirmButton.setObjectName(u"confirmButton")
        self.confirmButton.setGeometry(QRect(390, 150, 100, 40))
        self.confirmButton.setStyleSheet(u"border-image: url(\"components/page2/sub/images/1.png\");\n"
"margin: 0;")
        self.portRangeLabel = QLabel(NetworkPopup)
        self.portRangeLabel.setObjectName(u"portRangeLabel")
        self.portRangeLabel.setGeometry(QRect(170, 10, 71, 16))
        self.portRangeLabel.setStyleSheet(u"")
        self.portRangeLane = QLineEdit(NetworkPopup)
        self.portRangeLane.setObjectName(u"portRangeLane")
        self.portRangeLane.setGeometry(QRect(160, 30, 120, 30))
        self.portRangeLane.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;\n"
"")
        self.IpLabel = QLabel(NetworkPopup)
        self.IpLabel.setObjectName(u"IpLabel")
        self.IpLabel.setGeometry(QRect(20, 80, 71, 16))
        self.IpLabel.setStyleSheet(u"")
        self.IpLane = QLineEdit(NetworkPopup)
        self.IpLane.setObjectName(u"IpLane")
        self.IpLane.setGeometry(QRect(20, 100, 120, 30))
        self.IpLane.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;\n"
"")
        self.descriptionLabel = QLabel(NetworkPopup)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setGeometry(QRect(160, 80, 71, 16))
        self.descriptionLabel.setStyleSheet(u"")
        self.descriptionLane = QLineEdit(NetworkPopup)
        self.descriptionLane.setObjectName(u"descriptionLane")
        self.descriptionLane.setGeometry(QRect(160, 100, 120, 30))
        self.descriptionLane.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;\n"
"")

        self.retranslateUi(NetworkPopup)

        QMetaObject.connectSlotsByName(NetworkPopup)
    # setupUi

    def retranslateUi(self, NetworkPopup):
        NetworkPopup.setWindowTitle(QCoreApplication.translate("NetworkPopup", u"IP \ucd94\uac00", None))
        self.protocolLabel.setText(QCoreApplication.translate("NetworkPopup", u"Protocol", None))
        self.cancelButton.setText("")
        self.confirmButton.setText("")
        self.portRangeLabel.setText(QCoreApplication.translate("NetworkPopup", u"Port Range", None))
        self.IpLabel.setText(QCoreApplication.translate("NetworkPopup", u"Source IP", None))
        self.descriptionLabel.setText(QCoreApplication.translate("NetworkPopup", u"Description", None))
    # retranslateUi

