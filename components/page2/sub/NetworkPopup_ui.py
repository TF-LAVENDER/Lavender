# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NetworkPopup.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_NetworkPopup(object):
    def setupUi(self, NetworkPopup):
        if not NetworkPopup.objectName():
            NetworkPopup.setObjectName(u"NetworkPopup")
        NetworkPopup.resize(313, 184)
        NetworkPopup.setStyleSheet(u"background-color: #2d3242;")
        self.verticalLayout = QVBoxLayout(NetworkPopup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_ip = QLabel(NetworkPopup)
        self.label_ip.setObjectName(u"label_ip")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_ip)

        self.lineEdit_ip = QLineEdit(NetworkPopup)
        self.lineEdit_ip.setObjectName(u"lineEdit_ip")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_ip)

        self.label_status = QLabel(NetworkPopup)
        self.label_status.setObjectName(u"label_status")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_status)

        self.lineEdit_status = QLineEdit(NetworkPopup)
        self.lineEdit_status.setObjectName(u"lineEdit_status")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_status)

        self.label_time = QLabel(NetworkPopup)
        self.label_time.setObjectName(u"label_time")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_time)

        self.lineEdit_time = QLineEdit(NetworkPopup)
        self.lineEdit_time.setObjectName(u"lineEdit_time")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_time)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btn_ok = QPushButton(NetworkPopup)
        self.btn_ok.setObjectName(u"btn_ok")

        self.buttonLayout.addWidget(self.btn_ok)

        self.btn_cancel = QPushButton(NetworkPopup)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.buttonLayout.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(NetworkPopup)

        QMetaObject.connectSlotsByName(NetworkPopup)
    # setupUi

    def retranslateUi(self, NetworkPopup):
        NetworkPopup.setWindowTitle(QCoreApplication.translate("NetworkPopup", u"\ub370\uc774\ud130 \ucd94\uac00", None))
        self.label_ip.setText(QCoreApplication.translate("NetworkPopup", u"IP Address", None))
        self.label_status.setText(QCoreApplication.translate("NetworkPopup", u"Status", None))
        self.label_time.setText(QCoreApplication.translate("NetworkPopup", u"Time", None))
        self.btn_ok.setText(QCoreApplication.translate("NetworkPopup", u"\ud655\uc778", None))
        self.btn_cancel.setText(QCoreApplication.translate("NetworkPopup", u"\ucde8\uc18c", None))
    # retranslateUi

