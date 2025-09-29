import csv
import os
from PySide6.QtWidgets import QWidget
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
        self.ui.addBtn.clicked.connect(self.show_network_popup)
        self.ui.delBtn.clicked.connect(self.delete_selected_row)
        self.ui.blockedTableView.doubleClicked.connect(self.edit_selected_row)

        self.ui.blockedButton.setFlat(True)
        self.ui.allowedButton.setFlat(True)

        self.model = QStandardItemModel(0, 3)
        self.model.setHorizontalHeaderLabels(["프로토콜", "포트", "IP", "비고"])
        self.ui.blockedTableView.setModel(self.model)
        self.ui.blockedTableView.horizontalHeader().setStretchLastSection(True)

        self.load_from_csv()
    
    def menuChange(self, menuNum):
        self.ui.blockedButton.setStyleSheet(f"border-image: url('{resource_path('components/page2/images/blocked_off.png')}');")
        self.ui.allowedButton.setStyleSheet(f"border-image: url('{resource_path('components/page2/images/allowed_off.png')}');")
        if menuNum == 1:
            self.ui.blockedButton.setStyleSheet(f"border-image: url('{resource_path('components/page2/images/blocked_on.png')}');")
        elif menuNum == 2:
            self.ui.allowedButton.setStyleSheet(f"border-image: url('{resource_path('components/page2/images/allowed_on.png')}');")

    def blocked_clicked(self):
        self.menuChange(1)

    def allowed_clicked(self):
        self.menuChange(2)

    def show_network_popup(self):
        dialog = NetworkPopup(self)
        if dialog.exec():
            row_data = dialog.get_data()
            self.add_row(row_data)
            self.save_to_csv()  # 저장

    def add_row(self, row_data):
        items = [QStandardItem(field) for field in row_data]
        self.model.appendRow(items)
        port = row_data[1]  # 두 번째 컬럼이 PORT
        add_firewall_rule(port)

        

        

    def save_to_csv(self):
        with open("data.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for row in range(self.model.rowCount()):
                row_values = [
                    self.model.item(row, col).text() if self.model.item(row, col) else ""
                    for col in range(self.model.columnCount())
                ]
                writer.writerow(row_values)

    def load_from_csv(self):
        if not os.path.exists("data.csv"):
            return
        with open("data.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                self.add_row(row)

    def delete_selected_row(self):
        selection_model = self.ui.blockedTableView.selectionModel()
        indexes = selection_model.selectedRows()

        if not indexes:
            return

        for index in sorted(indexes, key=lambda x: x.row(), reverse=True):
            #self.model.removeRow(index.row())
            port_item = self.model.item(index.row(), 1)
            if port_item:
                delete_firewall_rule(port_item.text())  # 삭제 전에 포트 얻기
            self.model.removeRow(index.row())
        self.save_to_csv()
        
        # for index in sorted(indexes, key=lambda x: x.row(), reverse=True):
        #     port_item = self.model.item(index.row(), 1)
        #     if port_item:
        #         delete_firewall_rule(port_item.text())  # 삭제 전에 포트 얻기
        #     self.model.removeRow(index.row())

    def edit_selected_row(self, index):
        if not index.isValid():
            return

        row = index.row()
        current_data = [
            self.model.item(row, 0).text(),
            self.model.item(row, 1).text(),
            self.model.item(row, 2).text(),
            self.model.item(row, 3).text() if self.model.columnCount() > 3 else ""
        ]

        # 팝업 열고 기존 데이터 설정
        dialog = NetworkPopup(self)
        dialog.ui.protocolLane.setText(current_data[0])
        dialog.ui.portRangeLane.setText(current_data[1])
        dialog.ui.IpLane.setText(current_data[2])
        dialog.ui.descriptionLane.setText(current_data[3])

        if dialog.exec():
            new_data = dialog.get_data()
            for col, value in enumerate(new_data):
                self.model.setItem(row, col, QStandardItem(value))
            self.save_to_csv()        


def add_firewall_rule(port):
    rule_name = f"MyApp_Inbound_{port}"
    cmd = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        f"name={rule_name}",
        "dir=in", "action=allow",
        "protocol=TCP", f"localport={port}",
        "profile=any", "enable=yes"
    ]
    subprocess.run(cmd, shell=True)

def delete_firewall_rule(port):
    rule_name = f"MyApp_Inbound_{port}"
    cmd = [
        "netsh", "advfirewall", "firewall", "delete", "rule",
        f"name={rule_name}",
        "protocol=TCP", f"localport={port}"
    ]
    subprocess.run(cmd, shell=True)


        