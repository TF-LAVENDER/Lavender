import csv
import os
from datetime import datetime
from PySide6.QtWidgets import QWidget, QTableView, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from utils import load_ui_file, resource_path

class Page3(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = load_ui_file(resource_path("components/page3/page3.ui"))
        self.setLayout(self.ui.layout())

        # 로그 테이블 모델 설정
        self.model_logs = QStandardItemModel(0, 8)
        self.model_logs.setHorizontalHeaderLabels([
            "", "유형", "날짜", "송신 주소", "송신 포트", "수신 주소", "수신 포트", "비고"
        ])

        # 테이블 뷰 설정
        self.ui.logsTableView.setModel(self.model_logs)
        self.ui.logsTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.logsTableView.horizontalHeader().setFixedHeight(30)
        self.ui.logsTableView.verticalHeader().hide()
        
        # 컬럼 너비 설정
        self.ui.logsTableView.setColumnWidth(0, 45)   # 인덱스
        self.ui.logsTableView.setColumnWidth(1, 80)   # 유형
        self.ui.logsTableView.setColumnWidth(2, 140)  # 날짜
        self.ui.logsTableView.setColumnWidth(3, 120)  # 송신 주소
        self.ui.logsTableView.setColumnWidth(4, 80)   # 송신 포트
        self.ui.logsTableView.setColumnWidth(5, 120)  # 수신 주소
        self.ui.logsTableView.setColumnWidth(6, 80)   # 수신 포트
        self.ui.logsTableView.horizontalHeader().setStretchLastSection(True)  # 비고 컬럼

        # CSV 파일 로드
        self.load_logs_from_csv()

    def add_log_entry(self, log_data):
        """
        새로운 로그 항목 추가
        log_data: [유형, 송신주소, 송신포트, 수신주소, 수신포트, 비고]
        """
        # 현재 시간 추가
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # 인덱스는 현재 행 개수 + 1
        idx = self.model_logs.rowCount() + 1
        
        # 데이터 준비: [인덱스, 유형, 날짜, 송신주소, 송신포트, 수신주소, 수신포트, 비고]
        row_data = [str(idx), log_data[0], current_time] + log_data[1:]
        
        # 테이블에 추가
        items = [QStandardItem(field) for field in row_data]
        self.model_logs.appendRow(items)
        
        # 행 높이 설정
        self.ui.logsTableView.setRowHeight(self.model_logs.rowCount() - 1, 40)
        
        # 날짜별 CSV 파일에 저장
        self.save_logs_to_csv(current_date)

    def load_logs_from_csv(self):
        """오늘 날짜의 로그 파일에서 로그 데이터 로드"""
        current_date = datetime.now().strftime("%Y-%m-%d")
        csv_path = resource_path(f"logs/{current_date}.csv")
        
        if os.path.exists(csv_path):
            try:
                with open(csv_path, mode="r", newline="", encoding="utf-8") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if len(row) >= 8:  # 8개 컬럼이 모두 있는지 확인
                            items = [QStandardItem(field) for field in row]
                            self.model_logs.appendRow(items)
                            # 행 높이 설정
                            self.ui.logsTableView.setRowHeight(self.model_logs.rowCount() - 1, 40)
            except Exception as e:
                print(f"로그 파일 로드 중 오류: {e}")

    def save_logs_to_csv(self, date_str=None):
        """현재 로그 데이터를 날짜별 CSV 파일에 저장"""
        if date_str is None:
            date_str = datetime.now().strftime("%Y-%m-%d")
        
        # logs 디렉토리가 없으면 생성
        logs_dir = resource_path("logs")
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        
        csv_path = resource_path(f"logs/{date_str}.csv")
        
        try:
            with open(csv_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                for row in range(self.model_logs.rowCount()):
                    row_values = [
                        self.model_logs.item(row, col).text() if self.model_logs.item(row, col) else ""
                        for col in range(self.model_logs.columnCount())
                    ]
                    writer.writerow(row_values)
        except Exception as e:
            print(f"로그 파일 저장 중 오류: {e}")

    def clear_old_logs(self, days=30):
        """오래된 로그 자동 정리 (선택사항)"""
        # TODO: 날짜 기준으로 오래된 로그 삭제 구현
        pass

    def refresh_display(self):
        """테이블 새로고침"""
        self.ui.logsTableView.repaint()