from PySide6.QtWidgets import QDialog

from PySide6.QtWidgets import QDialog
from components.page2.sub.NetworkPopup_ui import Ui_NetworkPopup
from utils import resource_path

class NetworkPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NetworkPopup()
        self.ui.setupUi(self)

        self.setWindowTitle("네트워크 규칙 추가")
        self.setFixedSize(500, 200)

        self.ui.confirmButton.setStyleSheet(f"border-image: url('{resource_path('components/page2/sub/images/1.png')}');")
        self.ui.cancelButton.setStyleSheet(f"border-image: url('{resource_path('components/page2/sub/images/2.png')}');")

        self.ui.confirmButton.clicked.connect(self.accept)
        self.ui.cancelButton.clicked.connect(self.reject)

    def get_data(self):
        return [
            self.ui.protocolLane.text(),
            self.ui.portRangeLane.text(),
            self.ui.IpLane.text(),
        ]
