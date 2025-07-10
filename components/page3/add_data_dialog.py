from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLineEdit, 
                             QLabel, QPushButton, QComboBox, QMessageBox, QDateEdit)
from PySide6.QtCore import QDate
from datetime import datetime
from zoneinfo import ZoneInfo
import re

class AddDataDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add New Security Log Entry")
        self.setModal(True)
        self.setFixedSize(400, 320)
        self.setStyleSheet("""
            QDialog {
                background-color: #2d3242;
                color: white;
            }
            QLabel {
                color: white;
                font-weight: bold;
            }
            QLineEdit, QComboBox, QDateEdit {
                background-color: #111111;
                border: 2px solid #5056A5;
                border-radius: 5px;
                padding: 20px;
                color: white;
                font-size: 12px;
            }
            QLineEdit:focus, QComboBox:focus, QDateEdit:focus {
                border-color: #6066B5;
            }
            QPushButton {
                margin-top: 10px;
                background-color: #5056A5;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 4px 20px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #6066B5;
            }
            QPushButton:pressed {
                background-color: #4046A5;
            }
            QPushButton#cancelButton {
                background-color: #666;
            }
            QPushButton#cancelButton:hover {
                background-color: #777;
            }
        """)
        
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # IP Address input
        ip_label = QLabel("Source IP Address:")
        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("예: 192.168.1.100")
        layout.addWidget(ip_label)
        layout.addWidget(self.ip_input)
  
        # Event Type input
        event_label = QLabel("Event Type:")
        self.event_input = QComboBox()
        
        # 기본 이벤트 타입들
        default_event_types = [
            "illegal access",
            "Dos", 
            "illegal scan",
            "brute force",
            "malware",
            "phishing",
            "suspicious activity",
            "unauthorized login",
            "privilege escalation",
            "data exfiltration",
            "network intrusion",
            "system compromise"
        ]
        
        self.event_input.addItems(default_event_types)
        self.event_input.setEditable(True)
        layout.addWidget(event_label)
        layout.addWidget(self.event_input)
        
        # Description input
        desc_label = QLabel("Description:")
        self.desc_input = QLineEdit()
        self.desc_input.setPlaceholderText("예: Login attempt failed")
        layout.addWidget(desc_label)
        layout.addWidget(self.desc_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        self.add_button = QPushButton("Add Entry")
        self.add_button.clicked.connect(self.accept)
        
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setObjectName("cancelButton")
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.add_button)
        
        layout.addLayout(button_layout)
        
    def get_data(self):
        """입력된 데이터 반환"""
        return {
            'ip': self.ip_input.text().strip(),
            'date': datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y.%m.%d"),
            'event_type': self.event_input.currentText().strip(),
            'description': self.desc_input.text().strip()
        }
        
    def validate_ip_address(self, ip):
        """IP 주소 유효성 검사"""
        # IPv4 주소 패턴
        ipv4_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
        
        # IPv6 주소 패턴 (간단한 버전)
        ipv6_pattern = r'^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}'
        
        if re.match(ipv4_pattern, ip) or re.match(ipv6_pattern, ip):
            return True
        return False
        
    def validate_data(self):
        """입력 데이터 유효성 검사"""
        data = self.get_data()
        
        # IP 주소 검사
        if not data['ip']:
            QMessageBox.warning(self, "입력 오류", "IP 주소를 입력해주세요.")
            self.ip_input.setFocus()
            return False
            
        if not self.validate_ip_address(data['ip']):
            QMessageBox.warning(self, "입력 오류", "올바른 IP 주소 형식을 입력해주세요.\n예: 192.168.1.100")
            self.ip_input.setFocus()
            return False
            
        # 이벤트 타입 검사
        if not data['event_type']:
            QMessageBox.warning(self, "입력 오류", "이벤트 타입을 선택해주세요.")
            self.event_input.setFocus()
            return False
            
        # 설명 검사
        if not data['description']:
            QMessageBox.warning(self, "입력 오류", "설명을 입력해주세요.")
            self.desc_input.setFocus()
            return False
            
        # 설명 길이 검사
        if len(data['description']) > 255:
            QMessageBox.warning(self, "입력 오류", "설명은 255자 이하로 입력해주세요.")
            self.desc_input.setFocus()
            return False
            
        return True
        
    def accept(self):
        """다이얼로그 승인 처리"""
        if self.validate_data():
            super().accept()
            
    def reset_form(self):
        """폼 초기화"""
        self.ip_input.clear()
        self.event_input.setCurrentIndex(0)
        self.desc_input.clear()
        self.ip_input.setFocus()


class EditDataDialog(AddDataDialog):
    """데이터 편집용 다이얼로그 (AddDataDialog 상속)"""
    
    def __init__(self, parent=None, log_data=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Security Log Entry")
        self.log_data = log_data
        
        # 기존 데이터로 폼 채우기
        if log_data:
            self.populate_form(log_data)
            
        # 버튼 텍스트 변경
        self.add_button.setText("Update Entry")
        
    def populate_form(self, log_data):
        """기존 데이터로 폼 채우기"""
        if isinstance(log_data, dict):
            self.ip_input.setText(log_data.get('source_ip', ''))
            
            # 이벤트 타입 설정
            event_type = log_data.get('event_type', '')
            index = self.event_input.findText(event_type)
            if index >= 0:
                self.event_input.setCurrentIndex(index)
            else:
                self.event_input.setCurrentText(event_type)
                
            self.desc_input.setText(log_data.get('description', ''))
        elif isinstance(log_data, list) and len(log_data) >= 5:
            # 리스트 형태의 데이터 (테이블에서 직접 가져온 경우)
            self.ip_input.setText(log_data[1])  # source_ip
            
            # 이벤트 타입 설정
            event_type = log_data[3]  # event_type
            index = self.event_input.findText(event_type)
            if index >= 0:
                self.event_input.setCurrentIndex(index)
            else:
                self.event_input.setCurrentText(event_type)
                
            self.desc_input.setText(log_data[4])  # description