import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor
from page3_ui import Ui_Page3

class Page3(QWidget):
    COLORS = {
        'even_row_bg': QColor(69, 76, 135),     # 짙은 보라/파랑 (이미지 1,3,5 행 배경색)
        'odd_row_bg': QColor(57, 63, 110),      # 조금 더 짙은 파랑 (이미지 2,4,6 행 배경색)
        'even_row_fg': QColor(255, 255, 255),   # 흰색
        'odd_row_fg': QColor(255, 255, 255),    # 흰색
        'event_types': {
            'illegal access': QColor(255, 255, 255),  # 흰색 유지 (특별 강조는 없음)
            'Dos': QColor(255, 255, 255),
            'illegal scan': QColor(255, 255, 255)
        },
        'header_bg': QColor(39, 43, 77),        # 헤더 진한 파랑
        'header_fg': QColor(255, 255, 255)      # 헤더 흰색
    }

    COLUMN_WIDTHS = {
        0: 40,  # ASC 컬럼 좁게
        1: QHeaderView.ResizeMode.Stretch,
        2: QHeaderView.ResizeMode.Stretch,
        3: QHeaderView.ResizeMode.Stretch,
        4: QHeaderView.ResizeMode.Stretch,
    }

    ROW_HEIGHT = 35

    def __init__(self):
        super().__init__()
        self.ui = Ui_Page3()
        self.ui.setupUi(self)
        
        # 데이터 저장소 초기화
        self.sample_data = [
            ["182.168.10.1", "2025.25.25", "illegal access", "Description"],
            ["182.168.10.1", "2025.25.25", "Dos", "Description"],
            ["182.168.10.1", "2025.25.25", "illegal scan", "Description"],
            ["182.168.10.1", "2025.25.25", "illegal access", "Description"],
            ["182.168.10.1", "2025.25.25", "illegal access", "Description"],
            ["182.168.10.1", "2025.25.25", "illegal access", "Description"],
            ["182.168.10.1", "2025.25.25", "illegal access", "Description"],
        ]

        # 테이블 기본 스타일 시트 (헤더 및 그리드 등)
        self.ui.tableWidget.setStyleSheet(f"""
            QHeaderView::section {{
                background-color: rgb({self.COLORS['header_bg'].red()}, {self.COLORS['header_bg'].green()}, {self.COLORS['header_bg'].blue()});
                color: rgb({self.COLORS['header_fg'].red()}, {self.COLORS['header_fg'].green()}, {self.COLORS['header_fg'].blue()});
                font-weight: bold;
                height: 35px;
                border: none;
                padding: 5px;
            }}
            QTableWidget {{
                gridline-color: rgb(50, 55, 100);
                background-color: rgb(45, 50, 95);
                alternate-background-color: rgb(60, 65, 120);
            }}
            QTableWidget::item {{
                padding: 5px;
                border-bottom: 1px solid rgb(50, 55, 100);
            }}
            QTableWidget::item:selected {{
                background-color: rgb(70, 77, 140);
            }}
        """)
        self.ui.tableWidget.setAlternatingRowColors(False)  # 직접 색깔 컨트롤 할 예정

        self._setup_table()

    def _setup_table(self):
        """초기 테이블 설정 및 기본 데이터 로드"""
        self.ui.tableWidget.setRowCount(0)
        self.load_sample_data()
        self._configure_table_headers()

    def load_sample_data(self):
        """sample_data의 모든 항목을 테이블에 로드"""
        for row_data in self.sample_data:
            self.add_log_entry(*row_data)

    def add_sample_data(self, source_ip, date, event_type, description):
        """새로운 데이터를 sample_data에 추가하고 테이블에 표시"""
        new_data = [source_ip, date, event_type, description]
        self.sample_data.append(new_data)
        self.add_log_entry(*new_data)

    def insert_sample_data(self, index, source_ip, date, event_type, description):
        """특정 위치에 새로운 데이터를 sample_data에 삽입하고 테이블 재구성"""
        new_data = [source_ip, date, event_type, description]
        self.sample_data.insert(index, new_data)
        self.refresh_table()

    def remove_sample_data(self, index):
        """특정 인덱스의 데이터를 sample_data에서 제거하고 테이블 재구성"""
        if 0 <= index < len(self.sample_data):
            self.sample_data.pop(index)
            self.refresh_table()

    def update_sample_data(self, index, source_ip, date, event_type, description):
        """특정 인덱스의 데이터를 sample_data에서 수정하고 테이블 재구성"""
        if 0 <= index < len(self.sample_data):
            self.sample_data[index] = [source_ip, date, event_type, description]
            self.refresh_table()

    def get_sample_data(self):
        """현재 sample_data 반환"""
        return self.sample_data.copy()

    def set_sample_data(self, new_data):
        """sample_data를 새로운 데이터로 교체하고 테이블 재구성"""
        self.sample_data = new_data.copy()
        self.refresh_table()

    def refresh_table(self):
        """테이블을 완전히 새로고침"""
        self.ui.tableWidget.setRowCount(0)
        self.load_sample_data()

    def _configure_table_headers(self):
        header = self.ui.tableWidget.horizontalHeader()
        for col, width in self.COLUMN_WIDTHS.items():
            if width == QHeaderView.ResizeMode.Stretch:
                header.setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)
            else:
                header.setSectionResizeMode(col, QHeaderView.ResizeMode.Fixed)
                self.ui.tableWidget.setColumnWidth(col, width)

    def _create_table_item(self, value, row, col):
        item = QTableWidgetItem(str(value))
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 선택 및 활성화 가능

        # 행 배경색 (이미지 참고)
        row_bg = self.COLORS['even_row_bg'] if row % 2 == 0 else self.COLORS['odd_row_bg']
        row_fg = self.COLORS['even_row_fg'] if row % 2 == 0 else self.COLORS['odd_row_fg']

        # 이벤트 타입 컬럼만 별도 처리 (글자색 강조 등)
        if col == 3:  # Description 컬럼
            fg = self.COLORS['event_types'].get(value, row_fg)
            item.setBackground(row_bg)
            item.setForeground(fg)
        else:
            item.setBackground(row_bg)
            item.setForeground(row_fg)

        return item

    def add_log_entry(self, source_ip, date, event_type, description):
        try:
            current_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(current_row)

            row_data = [
                "1",  # ASC는 항상 1로 고정
                source_ip,
                date,
                event_type,
                description
            ]
            for col, value in enumerate(row_data):
                item = self._create_table_item(value, current_row, col)
                self.ui.tableWidget.setItem(current_row, col, item)

            self.ui.tableWidget.setRowHeight(current_row, self.ROW_HEIGHT)
        except Exception as e:
            print(f"Error adding log entry: {e}")

    def clear_logs(self):
        """테이블과 sample_data 모두 비우기"""
        self.ui.tableWidget.setRowCount(0)
        self.sample_data.clear()

    def get_selected_log(self):
        try:
            current_row = self.ui.tableWidget.currentRow()
            if current_row >= 0:
                return [
                    self.ui.tableWidget.item(current_row, col).text()
                    if self.ui.tableWidget.item(current_row, col) else ""
                    for col in range(self.ui.tableWidget.columnCount())
                ]
            return None
        except Exception as e:
            print(f"Error getting selected log: {e}")
            return None

    # 사용 예시를 위한 메서드들
    def demo_add_data(self):
        """데모용 데이터 추가 예시"""
        # 새로운 데이터 추가
        self.add_sample_data("192.168.1.100", "2025.01.07", "brute force", "Login attempt failed")
        self.add_sample_data("10.0.0.50", "2025.01.07", "malware", "Suspicious file detected")
        
    def demo_insert_data(self):
        """데모용 데이터 삽입 예시"""
        # 인덱스 2 위치에 새로운 데이터 삽입
        self.insert_sample_data(2, "172.16.0.1", "2025.01.07", "phishing", "Suspicious email link")
        
    def demo_update_data(self):
        """데모용 데이터 수정 예시"""
        # 인덱스 0의 데이터 수정
        self.update_sample_data(0, "192.168.1.1", "2025.01.07", "illegal access", "Updated description")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Page3()
    window.show()
    
    # 데모용 추가 데이터 테스트
    # window.demo_add_data()
    
    sys.exit(app.exec())