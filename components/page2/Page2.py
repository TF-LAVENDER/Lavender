import csv
import os
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem
from components.page2.sub.NetworkPopup import NetworkPopup
from utils import load_ui_file, resource_path

class SimpleTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self._headers = ["ASC", "IP", "Date", "Description"]

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

        self.ui.blockedButton.setFlat(True)
        self.ui.allowedButton.setFlat(True)

        self.model = QStandardItemModel(0, 3)
        self.model.setHorizontalHeaderLabels(["IP", "상태", "시간"])
        self.ui.blockedTableView.setModel(self.model)
        self.ui.blockedTableView.horizontalHeader().setStretchLastSection(True)

        self.load_from_csv()
    
    def menuChange(self, menuNum):
        self.ui.blockedButton.setStyleSheet("border-image: url('components/page2/images/blocked_off.png');")
        self.ui.allowedButton.setStyleSheet("border-image: url('components/page2/images/allowed_off.png');")
        if menuNum == 1:
            self.ui.blockedButton.setStyleSheet("border-image: url('components/page2/images/blocked_on.png');")
        elif menuNum == 2:
            self.ui.allowedButton.setStyleSheet("border-image: url('components/page2/images/allowed_on.png');")

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

