import csv
import os
from PySide6.QtWidgets import QWidget, QTableView, QHeaderView
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem
from components.page2.sub.NetworkPopup import NetworkPopup
from utils import load_ui_file, resource_path
import subprocess

class SimpleTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self._headers = ["PROTOCOL", "PORT", "IP", "Description"]

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return str(self._data[index.row()][index.column()])
        return None

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        return None

class Page2(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = load_ui_file(resource_path("components/page2/page2.ui"))
        self.setLayout(self.ui.layout())

        self.ui.blockedButton.clicked.connect(self.blocked_clicked)
        self.ui.allowedButton.clicked.connect(self.allowed_clicked)
        self.ui.addButton.clicked.connect(self.show_network_popup)
        self.ui.delButton.clicked.connect(self.delete_selected_row)

        self.ui.blockedButton.setFlat(True)
        self.ui.allowedButton.setFlat(True)

        self.model_blocked = QStandardItemModel(0, 5)
        self.model_blocked.setHorizontalHeaderLabels(["", "프로토콜", "포트", "IP", "비고"])
        self.model_allowed = QStandardItemModel(0, 5)
        self.model_allowed.setHorizontalHeaderLabels(["", "프로토콜", "포트", "IP", "비고"])

        self.current_mode = "blocked"  # blocked or allowed
        self.ui.blockedTableView.setModel(self.model_blocked)
        self.ui.blockedTableView.horizontalHeader().setStretchLastSection(True)
        self.ui.blockedTableView.verticalHeader().hide()
        self.ui.blockedTableView.setSelectionBehavior(QTableView.SelectRows)

        self.ui.blockedTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.blockedTableView.setColumnWidth(0, 45)
        self.ui.blockedTableView.setColumnWidth(1, 75)
        self.ui.blockedTableView.setColumnWidth(2, 75)
        self.ui.blockedTableView.setColumnWidth(3, 200) 

        self.load_from_csvs()

    def menuChange(self, menuNum):
        self.ui.blockedButton.setStyleSheet(f"border-image: url('{resource_path('components/page2/images/blocked_off.png')}');")
        self.ui.allowedButton.setStyleSheet(f"border-image: url('{resource_path('components/page2/images/allowed_off.png')}');")
        if menuNum == 1:
            self.ui.blockedButton.setStyleSheet(f"border-image: url('{resource_path('components/page2/images/blocked_on.png')}');")
            self.ui.blockedTableView.setModel(self.model_blocked)
            self.current_mode = "blocked"
        elif menuNum == 2:
            self.ui.allowedButton.setStyleSheet(f"border-image: url('{resource_path('components/page2/images/allowed_on.png')}');")
            self.ui.blockedTableView.setModel(self.model_allowed)
            self.current_mode = "allowed"

    def blocked_clicked(self):
        self.menuChange(1)

    def allowed_clicked(self):
        self.menuChange(2)

    def show_network_popup(self):
        dialog = NetworkPopup(self)
        if dialog.exec():
            row_data = dialog.get_data()
            self.add_row(row_data)
            self.save_to_csvs()  # 저장

    def add_row(self, row_data):
        # 인덱스는 현재 행 개수 + 1
        if self.current_mode == "blocked":
            idx = self.model_blocked.rowCount() + 1
            items = [QStandardItem(str(idx))] + [QStandardItem(field) for field in row_data]
            self.model_blocked.appendRow(items)
        else:
            idx = self.model_allowed.rowCount() + 1
            items = [QStandardItem(str(idx))] + [QStandardItem(field) for field in row_data]
            self.model_allowed.appendRow(items)

    def save_to_csvs(self):
        with open(resource_path("data/blocked.csv"), mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for row in range(self.model_blocked.rowCount()):
                row_values = [
                    self.model_blocked.item(row, col).text() if self.model_blocked.item(row, col) else ""
                    for col in range(self.model_blocked.columnCount())
                ]
                writer.writerow(row_values)
        with open(resource_path("data/allowed.csv"), mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for row in range(self.model_allowed.rowCount()):
                row_values = [
                    self.model_allowed.item(row, col).text() if self.model_allowed.item(row, col) else ""
                    for col in range(self.model_allowed.columnCount())
                ]
                writer.writerow(row_values)

    def load_from_csvs(self):
        # blocked
        if os.path.exists(resource_path("data/blocked.csv")):
            with open(resource_path("data/blocked.csv"), mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                idx = 1
                for row in reader:
                    # 기존 csv에 인덱스 컬럼이 없으면 자동 부여
                    if len(row) == 4:
                        items = [QStandardItem(str(idx))] + [QStandardItem(field) for field in row]
                    else:
                        items = [QStandardItem(field) for field in row]
                    self.model_blocked.appendRow(items)
                    idx += 1
        # allowed
        if os.path.exists(resource_path("data/allowed.csv")):
            with open(resource_path("data/allowed.csv"), mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                idx = 1
                for row in reader:
                    if len(row) == 4:
                        items = [QStandardItem(str(idx))] + [QStandardItem(field) for field in row]
                    else:
                        items = [QStandardItem(field) for field in row]
                    self.model_allowed.appendRow(items)
                    idx += 1

    def delete_selected_row(self):
        selection_model = self.ui.blockedTableView.selectionModel()
        indexes = selection_model.selectedRows()

        if not indexes:
            return

        model = self.model_blocked if self.current_mode == "blocked" else self.model_allowed
        for index in sorted(indexes, key=lambda x: x.row(), reverse=True):
            port_item = model.item(index.row(), 2)  # 인덱스 컬럼 추가로 포트는 2번 인덱스
            if port_item and self.current_mode == "blocked":
                delete_firewall_rule(port_item.text())  # 삭제 전에 포트 얻기
            model.removeRow(index.row())
        # 삭제 후 인덱스 재정렬
        for row in range(model.rowCount()):
            model.setItem(row, 0, QStandardItem(str(row + 1)))
        self.save_to_csvs()

    def edit_selected_row(self, index):
        if not index.isValid():
            return

        model = self.model_blocked if self.current_mode == "blocked" else self.model_allowed
        row = index.row()
        current_data = [
            model.item(row, 1).text(),  # 프로토콜
            model.item(row, 2).text(),  # 포트
            model.item(row, 3).text(),  # IP
            model.item(row, 4).text() if model.columnCount() > 4 else ""  # 비고
        ]

        # 팝업 열고 기존 데이터 설정
        dialog = NetworkPopup(self)
        dialog.ui.protocolLane.setText(current_data[0])
        dialog.ui.portRangeLane.setText(current_data[1])
        dialog.ui.IpLane.setText(current_data[2])
        dialog.ui.descriptionLane.setText(current_data[3])

        if dialog.exec():
            new_data = dialog.get_data()
            # 인덱스는 그대로 두고 나머지 값만 수정
            for col, value in enumerate(new_data):
                model.setItem(row, col + 1, QStandardItem(value))
            self.save_to_csvs()


def add_firewall_rule(port):
    rule_name = f"MyApp_Inbound_{port}"
    cmd = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        f"name={rule_name}",
        "dir=in", "action=allow",
        "protocol=TCP", f"localport={port}",
        "profile=any", "enable=yes"
    ]
    ## 검증 안 됨 주석 해제 유의
    # mac_linux_cmd = [
    #     "sudo", "iptables", "-A", "INPUT", "-p", "tcp", "--dport", str(port), "-j", "ACCEPT"
    # ]
    subprocess.run(cmd, shell=True)

def delete_firewall_rule(port):
    rule_name = f"MyApp_Inbound_{port}"
    cmd = [
        "netsh", "advfirewall", "firewall", "delete", "rule",
        f"name={rule_name}",
        "protocol=TCP", f"localport={port}"
    ]
    ## 검증 안 됨 주석 해제 유의
    # mac_linux_cmd = [
    #     "sudo", "iptables", "-D", "INPUT", "-p", "tcp", "--dport", str(port), "-j", "ACCEPT"
    # ]
    subprocess.run(cmd, shell=True)

