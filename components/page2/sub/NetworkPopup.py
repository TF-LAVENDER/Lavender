from PySide6.QtWidgets import QDialog, QComboBox
import ipaddress

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

        # 프로토콜 드롭다운 설정
        self.setup_protocol_dropdown()

        port_regex = QRegularExpression(r"^\d{1,5}$")
        self.ui.portRangeLane.setValidator(QRegularExpressionValidator(port_regex))

        # CIDR 표기법을 지원하는 IP 주소 정규식 (예: 192.168.1.1 또는 192.168.1.0/24)
        ip_cidr_regex = QRegularExpression(r"^(?:(?:[0-9]{1,3}\.){3}[0-9]{1,3})(?:\/(?:[0-9]|[1-2][0-9]|3[0-2]))?$")
        self.ui.ipLane.setValidator(QRegularExpressionValidator(ip_cidr_regex))

        self.ui.confirmButton.clicked.connect(self.on_confirm)
        self.ui.cancelButton.clicked.connect(self.reject)

    def setup_protocol_dropdown(self):
        """프로토콜 드롭다운 설정"""
        # 기존 LineEdit를 ComboBox로 교체
        if hasattr(self.ui, 'protocolLane'):
            # 기존 위치와 크기 저장
            geometry = self.ui.protocolLane.geometry()
            parent = self.ui.protocolLane.parent()
            
            # ComboBox 생성
            self.protocol_combo = QComboBox(parent)
            self.protocol_combo.setGeometry(geometry)
            self.protocol_combo.addItems(["TCP", "UDP"])
            self.protocol_combo.setCurrentText("TCP")
            
            # ProtocolLane과 동일한 기본 스타일 적용 (화살표와 메뉴는 기본 유지)
            self.protocol_combo.setStyleSheet("""
                QComboBox {
                    border: 1px solid white;
                    border-radius: 10px;
                    color: #ffffff;
                    background-color: transparent;
                    padding: 5px 10px;
                }
            """)
            
            # 기존 LineEdit 숨기기
            self.ui.protocolLane.hide()

    def validate_ip_cidr(self, ip_input):
        """
        IP 주소 또는 CIDR 표기법 검증
        지원 형식: 192.168.1.1, 192.168.1.0/24
        """
        try:
            # ipaddress 모듈을 사용하여 검증
            ipaddress.ip_network(ip_input, strict=False)
            return True
        except ValueError:
            return False

    def on_confirm(self):
        port = self.ui.portRangeLane.text()
        ip = self.ui.IpLane.text()
        if not port.isdigit():
            QMessageBox.warning(self, "입력 오류", "포트는 숫자만 입력하세요.")
            return
        if not (0 <= int(port) <= 65535):
            QMessageBox.warning(self, "입력 오류", "포트는 0~65535 사이여야 합니다.")
            return
        
        # CIDR 표기법 지원 IP 주소 검증
        if not self.validate_ip_cidr(ip):
            QMessageBox.warning(self, "입력 오류", 
                              "IP 주소 형식이 올바르지 않습니다.\n"
                              "예시: 192.168.1.1 또는 192.168.1.0/24")
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
            self.protocol_combo.currentText(),
            self.ui.portRangeLane.text(),
            self.ui.ipLane.text(),
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
        