# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page3.ui'
## Created by: Qt User Interface Compiler version 6.9.0
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QAbstractItemView, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
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
        self.headerWidget.setStyleSheet(u"background-color: #272b4d; color: white;")
        self.headerLayout = QHBoxLayout(self.headerWidget)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(20, 0, 20, 0)

        self.toggleWidget = QWidget(self.headerWidget)
        self.toggleWidget.setMinimumSize(200, 30)
        self.toggleWidget.setMaximumSize(200, 30)
        self.toggleWidget.setObjectName(u"toggleWidget")
        self.toggleWidget.setStyleSheet("background-color: #5056A5; border-radius: 15px;")

        self.toggleLayout = QHBoxLayout(self.toggleWidget)
        self.toggleLayout.setObjectName(u"toggleLayout")
        self.toggleLayout.setSpacing(0)
        self.toggleLayout.setContentsMargins(0, 0, 0, 0)

        self.blockedButton = QPushButton(self.toggleWidget)
        self.blockedButton.setObjectName(u"blockedButton")
        self.blockedButton.setMinimumSize(QSize(100, 30))
        self.blockedButton.setMaximumSize(QSize(100, 30))
        self.blockedButton.setCheckable(True)
        self.toggleLayout.addWidget(self.blockedButton)

        self.allowedButton = QPushButton(self.toggleWidget)
        self.allowedButton.setObjectName(u"allowedButton")
        self.allowedButton.setMinimumSize(QSize(100, 30))
        self.allowedButton.setMaximumSize(QSize(100, 30))
        self.allowedButton.setCheckable(True)
        self.toggleLayout.addWidget(self.allowedButton)

        self.headerLayout.addWidget(self.toggleWidget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.headerLayout.addItem(self.horizontalSpacer)

        self.verticalLayout.addWidget(self.headerWidget)

        self.tableWidget = QTableWidget(Page3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["ASC", "IP", "Date", "Description", "Description"])
        self.tableWidget.setStyleSheet(u"""
            QTableWidget {
                gridline-color: rgb(50, 55, 100);
                background-color: rgb(45, 50, 95);
                alternate-background-color: rgb(68, 64, 122);
            }
            QTableWidget::item {
                padding: 5px;
                border-bottom: 1px solid rgb(50, 55, 100);
            }
            QHeaderView::section {
                background-color: rgb(39, 43, 77);
                color: white;
                padding: 5px;
                border: none;
                font-weight: bold;
            }
            QTableWidget::item:selected {
                background-color: rgb(70, 77, 140);
            }
        """)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Page3)
        QMetaObject.connectSlotsByName(Page3)

        # ✅ 버튼 스타일과 체크 상태 즉시 반영 함수
        def updateToggleStyles(selected: str):
            if selected == "blocked":
                self.blockedButton.setChecked(True)
                self.allowedButton.setChecked(False)
            else:
                self.blockedButton.setChecked(False)
                self.allowedButton.setChecked(True)

            self.blockedButton.setStyleSheet(f"""
                QPushButton {{
                    background-color: {"#5056A5" if self.blockedButton.isChecked() else "#272b4d"};
                    border-top-left-radius: 15px;
                    border-bottom-left-radius: 15px;
                    border-top-right-radius: 0px;
                    border-bottom-right-radius: 0px;
                    color: white;
                    font-weight: bold;
                    border: none;
                }}
            """)
            self.allowedButton.setStyleSheet(f"""
                QPushButton {{
                    background-color: {"#5056A5" if self.allowedButton.isChecked() else "#272b4d"};
                    border-top-left-radius: 0px;
                    border-bottom-left-radius: 0px;
                    border-top-right-radius: 15px;
                    border-bottom-right-radius: 15px;
                    color: white;
                    font-weight: bold;
                    border: none;
                }}
            """)

        # ✅ 연결: 클릭 시 버튼 상태 업데이트
        self.blockedButton.clicked.connect(lambda: updateToggleStyles("blocked"))
        self.allowedButton.clicked.connect(lambda: updateToggleStyles("allowed"))

        updateToggleStyles("blocked")  # 초기 상태

    def retranslateUi(self, Page3):
        Page3.setWindowTitle(QCoreApplication.translate("Page3", u"Security Log", None))
        self.blockedButton.setText(QCoreApplication.translate("Page3", u"🔴 Blocked", None))
        self.allowedButton.setText(QCoreApplication.translate("Page3", u"🟢 Allowed", None))
