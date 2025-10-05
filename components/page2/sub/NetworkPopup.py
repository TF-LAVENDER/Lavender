from PySide6.QtWidgets import QDialog

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from utils import resource_path, load_ui_file

class NetworkPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = load_ui_file(resource_path("components/page2/sub/NetworkPopup.ui"))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.setParent(self)
        self.ui.setGeometry(0, 0, self.ui.width(), self.ui.height())

        self.setWindowTitle("네트워크 규칙 추가")
        self.setFixedSize(self.ui.size())

        port_regex = QRegularExpression(r"^\d{1,5}$")
        self.ui.portRangeLane.setValidator(QRegularExpressionValidator(port_regex))

        ipv4_regex = QRegularExpression(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        self.ui.IpLane.setValidator(QRegularExpressionValidator(ipv4_regex))

        self.ui.confirmButton.clicked.connect(self.on_confirm)
        self.ui.cancelButton.clicked.connect(self.reject)

    def on_confirm(self):
        port = self.ui.portRangeLane.text()
        ip = self.ui.IpLane.text()
        if not port.isdigit():
            QMessageBox.warning(self, "입력 오류", "포트는 숫자만 입력하세요.")
            return
        if not (0 <= int(port) <= 65535):
            QMessageBox.warning(self, "입력 오류", "포트는 0~65535 사이여야 합니다.")
            return
        # IPv4 형식 및 각 옥텟 0~255 검사
        octets = ip.split('.')
        if len(octets) != 4 or not all(o.isdigit() for o in octets):
            QMessageBox.warning(self, "입력 오류", "IP는 IPv4 형식으로 입력하세요.")
            return
        if not all(0 <= int(o) <= 255 for o in octets):
            QMessageBox.warning(self, "입력 오류", "IP 각 옥텟은 0~255 사이여야 합니다.")
            return
        self.accept()
    
    def keyPressEvent(self, event):
        from PySide6.QtCore import Qt
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.accept()
        else:
            super().keyPressEvent(event)

    def get_data(self):
        return [
            self.ui.protocolLane.text(),
            self.ui.portRangeLane.text(),
            self.ui.IpLane.text(),
            self.ui.descriptionLane.text()
        ]

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.old_pos = None