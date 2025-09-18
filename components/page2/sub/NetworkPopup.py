from PySide6.QtWidgets import QDialog

from PySide6.QtWidgets import QDialog
from components.page2.sub.NetworkPopup_ui import Ui_NetworkPopup

class NetworkPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NetworkPopup()  # ⬅️ 클래스 이름이 다르면 실제로 맞게 수정
        self.ui.setupUi(self)

        self.setWindowTitle("네트워크 규칙 추가")
        self.setFixedSize(300, 180)

        self.ui.btn_ok.clicked.connect(self.accept)
        self.ui.btn_cancel.clicked.connect(self.reject)

    def get_data(self):
        return [
            self.ui.lineEdit_ip.text(),
            self.ui.lineEdit_status.text(),
            self.ui.lineEdit_time.text()
        ]
