import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView, QPushButton, QMessageBox, QMenu
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QAction
from components.page3.page3_ui import Ui_Page3
from components.page3.add_data_dialog import AddDataDialog
from components.page3.database_manager import DatabaseManager

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
        
        # 데이터베이스 매니저 초기화
        try:
            self.db_manager = DatabaseManager()
            print("데이터베이스 초기화 완료")
        except Exception as e:
            QMessageBox.critical(self, "데이터베이스 오류", f"데이터베이스 초기화 실패: {str(e)}")
            sys.exit(1)

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

        # 버튼 추가
        self.add_add_button()
        self.add_delete_button()
        
        # 테이블 우클릭 메뉴 설정
        self.setup_context_menu()
        
        self._setup_table()

    def add_add_button(self):
        """헤더에 Add Data 버튼 추가"""
        # Add Data 버튼 생성
        self.add_data_button = QPushButton("+ Add Data")
        self.add_data_button.setMinimumSize(100, 30)
        self.add_data_button.setMaximumSize(100, 30)
        self.add_data_button.setStyleSheet("""
            QPushButton {
                background-color: #5056A5;
                border-radius: 15px;
                color: white;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #6066B5;
            }
            QPushButton:pressed {
                background-color: #4046A5;
            }
        """)
        self.add_data_button.clicked.connect(self.open_add_data_dialog)
        
        # 기존 헤더 레이아웃에 버튼 추가
        # blocked widget과 allowed widget 사이에 버튼 삽입
        self.ui.headerLayout.insertWidget(1, self.add_data_button)

    def add_delete_button(self):
        """헤더에 Delete 버튼들 추가"""
        # Delete Selected 버튼 생성
        self.delete_button = QPushButton("🗑 Delete Selected")
        self.delete_button.setMinimumSize(120, 30)
        self.delete_button.setMaximumSize(120, 30)
        self.delete_button.setStyleSheet("""
            QPushButton {
                background-color: #D32F2F;
                border-radius: 15px;
                color: white;
                font-weight: bold;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #F44336;
            }
            QPushButton:pressed {
                background-color: #B71C1C;
            }
        """)
        self.delete_button.clicked.connect(self.delete_selected_logs)
        
        # 헤더 레이아웃에 Delete 버튼들 추가
        self.ui.headerLayout.insertWidget(2, self.delete_button)

    def setup_context_menu(self):
        """테이블 우클릭 컨텍스트 메뉴 설정"""
        self.ui.tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableWidget.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, position):
        """컨텍스트 메뉴 표시"""
        if self.ui.tableWidget.itemAt(position) is None:
            return
            
        context_menu = QMenu(self)
        
        # 선택된 행 수 확인
        selected_rows = self.get_selected_rows()
        
        if len(selected_rows) == 1:
            # 단일 선택 시 메뉴
            delete_action = QAction("Delete Row", self)
            delete_action.triggered.connect(self.delete_selected_logs)
            context_menu.addAction(delete_action)
        elif len(selected_rows) > 1:
            # 다중 선택 시 메뉴
            delete_action = QAction(f"Delete {len(selected_rows)} Rows", self)
            delete_action.triggered.connect(self.delete_selected_logs)
            context_menu.addAction(delete_action)
        
        context_menu.addSeparator()
        
        
        # 메뉴 표시
        context_menu.exec(self.ui.tableWidget.mapToGlobal(position))

    def open_add_data_dialog(self):
        """데이터 추가 다이얼로그 열기"""
        dialog = AddDataDialog(self)
        if dialog.exec() == dialog.DialogCode.Accepted:
            data = dialog.get_data()
            
            try:
                # 데이터베이스에 데이터 추가
                log_id = self.db_manager.add_log_entry(
                    data['ip'], 
                    data['date'], 
                    data['event_type'], 
                    data['description']
                )
                
                # 테이블 새로고침
                self.load_data_from_db()
                
                # 성공 메시지 표시
                QMessageBox.information(self, "성공", "새로운 보안 로그 엔트리가 추가되었습니다.")
                
            except Exception as e:
                QMessageBox.critical(self, "오류", f"데이터 추가 실패: {str(e)}")

    def _setup_table(self):
        """초기 테이블 설정 및 기본 데이터 로드"""
        self.ui.tableWidget.setRowCount(0)
        self._configure_table_headers()
        # 테이블 선택 모드 설정 (행 단위 선택, 다중 선택 가능)
        self.ui.tableWidget.setSelectionBehavior(self.ui.tableWidget.SelectionBehavior.SelectRows)
        self.ui.tableWidget.setSelectionMode(self.ui.tableWidget.SelectionMode.ExtendedSelection)
        self.load_data_from_db()

    def load_data_from_db(self):
        """데이터베이스에서 데이터를 로드하여 테이블에 표시"""
        try:
            # 기존 테이블 데이터 클리어
            self.ui.tableWidget.setRowCount(0)
            
            # 데이터베이스에서 모든 로그 조회
            logs = self.db_manager.get_all_logs()
            
            # 각 로그를 테이블에 추가
            for log in logs:
                self.add_log_entry_to_table(
                    log['id'],
                    log['source_ip'],
                    log['date'],
                    log['event_type'],
                    log['description'],
                    log['id']  # 데이터베이스 ID도 저장
                )
                
        except Exception as e:
            QMessageBox.critical(self, "데이터베이스 오류", f"데이터 로드 실패: {str(e)}")

    def _configure_table_headers(self):
        header = self.ui.tableWidget.horizontalHeader()
        for col, width in self.COLUMN_WIDTHS.items():
            if width == QHeaderView.ResizeMode.Stretch:
                header.setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)
            else:
                header.setSectionResizeMode(col, QHeaderView.ResizeMode.Fixed)
                self.ui.tableWidget.setColumnWidth(col, width)

    def _create_table_item(self, value, row, col, log_id=None):
        item = QTableWidgetItem(str(value))
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 선택 및 활성화 가능

        # 데이터베이스 ID를 아이템 데이터로 저장 (첫 번째 컬럼에만)
        if col == 0 and log_id is not None:
            item.setData(Qt.ItemDataRole.UserRole, log_id)

        # 행 배경색 (이미지 참고)
        row_bg = self.COLORS['even_row_bg'] if row % 2 == 0 else self.COLORS['odd_row_bg']
        row_fg = self.COLORS['even_row_fg'] if row % 2 == 0 else self.COLORS['odd_row_fg']

        # 이벤트 타입 컬럼만 별도 처리 (글자색 강조 등)
        if col == 3:  # Event Type 컬럼
            fg = self.COLORS['event_types'].get(value, row_fg)
            item.setBackground(row_bg)
            item.setForeground(fg)
        else:
            item.setBackground(row_bg)
            item.setForeground(row_fg)

        return item

    def add_log_entry_to_table(self, id, source_ip, date, event_type, description, log_id=None):
        """테이블에 로그 엔트리 추가"""
        try:
            current_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(current_row)

            row_data = [
                id,  # ASC는 항상 1로 고정
                source_ip,
                date,
                event_type,
                description
            ]
            
            for col, value in enumerate(row_data):
                item = self._create_table_item(value, current_row, col, log_id if col == 0 else None)
                self.ui.tableWidget.setItem(current_row, col, item)

            self.ui.tableWidget.setRowHeight(current_row, self.ROW_HEIGHT)
            
        except Exception as e:
            print(f"Error adding log entry to table: {e}")

    def clear_logs(self):
        """테이블과 데이터베이스 모두 비우기"""
        try:
            reply = QMessageBox.question(
                self, 
                "확인", 
                "모든 로그를 삭제하시겠습니까?\n이 작업은 되돌릴 수 없습니다.",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                self.db_manager.clear_all_logs()
                self.ui.tableWidget.setRowCount(0)
                QMessageBox.information(self, "완료", "모든 로그가 삭제되었습니다.")
                
        except Exception as e:
            QMessageBox.critical(self, "오류", f"로그 삭제 실패: {str(e)}")

    def get_selected_log(self):
        """선택된 로그 정보 반환"""
        try:
            current_row = self.ui.tableWidget.currentRow()
            if current_row >= 0:
                # 첫 번째 컬럼에서 데이터베이스 ID 가져오기
                first_item = self.ui.tableWidget.item(current_row, 0)
                if first_item:
                    log_id = first_item.data(Qt.ItemDataRole.UserRole)
                    if log_id:
                        # 데이터베이스에서 해당 로그 정보 조회
                        return self.db_manager.get_log_by_id(log_id)
                
                # 백업: 테이블에서 직접 데이터 가져오기
                return [
                    self.ui.tableWidget.item(current_row, col).text()
                    if self.ui.tableWidget.item(current_row, col) else ""
                    for col in range(self.ui.tableWidget.columnCount())
                ]
            return None
        except Exception as e:
            print(f"Error getting selected log: {e}")
            return None

    def get_selected_rows(self):
        """선택된 행 번호들 반환"""
        selected_rows = set()
        for item in self.ui.tableWidget.selectedItems():
            selected_rows.add(item.row())
        return list(selected_rows)

    def get_selected_log_ids(self):
        """선택된 행들의 데이터베이스 ID들 반환"""
        selected_rows = self.get_selected_rows()
        log_ids = []
        
        for row in selected_rows:
            first_item = self.ui.tableWidget.item(row, 0)
            if first_item:
                log_id = first_item.data(Qt.ItemDataRole.UserRole)
                if log_id:
                    log_ids.append(log_id)
        
        return log_ids

    def delete_selected_logs(self):
        """선택된 로그들 삭제 (다중 선택 지원)"""
        try:
            selected_rows = self.get_selected_rows()
            
            if not selected_rows:
                QMessageBox.information(self, "안내", "삭제할 로그를 선택해주세요.")
                return
            
            # 선택된 로그들의 정보 수집
            log_info = []
            log_ids = []
            
            for row in selected_rows:
                first_item = self.ui.tableWidget.item(row, 0)
                if first_item:
                    log_id = first_item.data(Qt.ItemDataRole.UserRole)
                    if log_id:
                        log_ids.append(log_id)
                        source_ip = self.ui.tableWidget.item(row, 1).text()
                        event_type = self.ui.tableWidget.item(row, 3).text()
                        log_info.append(f"• {source_ip} - {event_type}")
            
            if not log_ids:
                QMessageBox.warning(self, "오류", "선택된 로그의 ID를 찾을 수 없습니다.")
                return
            
            # 확인 메시지 생성
            if len(log_ids) == 1:
                message = f"다음 로그를 삭제하시겠습니까?\n\n{log_info[0]}\n\n이 작업은 되돌릴 수 없습니다."
            else:
                message = f"{len(log_ids)}개의 로그를 삭제하시겠습니까?\n\n"
                message += "\n".join(log_info[:5])  # 최대 5개만 표시
                if len(log_info) > 5:
                    message += f"\n... 및 {len(log_info) - 5}개 더"
                message += "\n\n이 작업은 되돌릴 수 없습니다."
            
            reply = QMessageBox.question(
                self, 
                "삭제 확인", 
                message,
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                deleted_count = 0
                for log_id in log_ids:
                    if self.db_manager.delete_log_entry(log_id):
                        deleted_count += 1
                
                self.load_data_from_db()  # 테이블 새로고침
                
                if deleted_count == len(log_ids):
                    QMessageBox.information(self, "완료", f"{deleted_count}개의 로그가 성공적으로 삭제되었습니다.")
                else:
                    QMessageBox.warning(self, "부분 완료", f"{deleted_count}/{len(log_ids)}개의 로그가 삭제되었습니다.")
                
        except Exception as e:
            QMessageBox.critical(self, "오류", f"로그 삭제 실패: {str(e)}")

    def delete_multiple_logs(self):
        """여러 로그 삭제 (확장 기능) - 이제 delete_selected_logs로 대체됨"""
        self.delete_selected_logs()

    def get_all_unique_ips(self):
        """데이터베이스에서 모든 고유 IP 가져오기"""
        try:
            with self.db_manager.db_path:
                import sqlite3
                conn = sqlite3.connect(self.db_manager.db_path)
                cursor = conn.cursor()
                cursor.execute("SELECT DISTINCT source_ip FROM security_logs ORDER BY source_ip")
                ips = [row[0] for row in cursor.fetchall()]
                conn.close()
                return ips
        except Exception as e:
            print(f"Error getting unique IPs: {e}")
            return []

    def get_ip_log_counts(self):
        """IP별 로그 개수 반환"""
        try:
            with self.db_manager.db_path:
                import sqlite3
                conn = sqlite3.connect(self.db_manager.db_path)
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT source_ip, COUNT(*) 
                    FROM security_logs 
                    GROUP BY source_ip
                """)
                counts = dict(cursor.fetchall())
                conn.close()
                return counts
        except Exception as e:
            print(f"Error getting IP counts: {e}")
            return {}

    def delete_logs_by_ips(self, ip_list):
        """특정 IP들의 모든 로그 삭제"""
        try:
            if not ip_list:
                return
            
            # 각 IP별 로그 개수 확인
            total_logs = 0
            ip_info = []
            
            for ip in ip_list:
                logs = self.db_manager.search_logs(search_term=ip)
                count = len([log for log in logs if log['source_ip'] == ip])
                if count > 0:
                    total_logs += count
                    ip_info.append(f"• {ip}: {count}개 로그")
            
            if total_logs == 0:
                QMessageBox.information(self, "안내", "선택된 IP에 해당하는 로그가 없습니다.")
                return
            
            # 확인 메시지
            message = f"다음 IP들의 모든 로그를 삭제하시겠습니까?\n\n"
            message += "\n".join(ip_info)
            message += f"\n\n총 {total_logs}개의 로그가 삭제됩니다.\n이 작업은 되돌릴 수 없습니다."
            
            reply = QMessageBox.question(
                self,
                "IP별 삭제 확인",
                message,
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                deleted_count = 0
                
                # 각 IP별로 로그 삭제
                for ip in ip_list:
                    logs = self.db_manager.search_logs(search_term=ip)
                    ip_logs = [log for log in logs if log['source_ip'] == ip]
                    
                    for log in ip_logs:
                        if self.db_manager.delete_log_entry(log['id']):
                            deleted_count += 1
                
                self.load_data_from_db()  # 테이블 새로고침
                
                if deleted_count == total_logs:
                    QMessageBox.information(self, "완료", f"{deleted_count}개의 로그가 성공적으로 삭제되었습니다.")
                else:
                    QMessageBox.warning(self, "부분 완료", f"{deleted_count}/{total_logs}개의 로그가 삭제되었습니다.")
                
        except Exception as e:
            QMessageBox.critical(self, "오류", f"IP별 로그 삭제 실패: {str(e)}")

    def search_logs(self, search_term="", event_type="", start_date="", end_date=""):
        """로그 검색"""
        try:
            # 검색 조건이 모두 비어있으면 전체 로그 표시
            if not any([search_term, event_type, start_date, end_date]):
                self.load_data_from_db()
                return
            
            # 데이터베이스에서 검색
            logs = self.db_manager.search_logs(
                search_term=search_term if search_term else None,
                event_type=event_type if event_type else None,
                start_date=start_date if start_date else None,
                end_date=end_date if end_date else None
            )
            
            # 테이블 클리어
            self.ui.tableWidget.setRowCount(0)
            
            # 검색 결과를 테이블에 추가
            for log in logs:
                self.add_log_entry_to_table(
                    log['id'],
                    log['source_ip'],
                    log['date'],
                    log['event_type'],
                    log['description'],
                    log['id']
                )
                
        except Exception as e:
            QMessageBox.critical(self, "검색 오류", f"검색 실패: {str(e)}")

    def get_log_count(self):
        """총 로그 수 반환"""
        try:
            return self.db_manager.get_log_count()
        except Exception as e:
            print(f"Error getting log count: {e}")
            return 0

    def get_event_types(self):
        """모든 이벤트 타입 반환"""
        try:
            return self.db_manager.get_event_types()
        except Exception as e:
            print(f"Error getting event types: {e}")
            return []

    def backup_database(self, backup_path):
        """데이터베이스 백업"""
        try:
            if self.db_manager.backup_database(backup_path):
                QMessageBox.information(self, "완료", "데이터베이스 백업이 완료되었습니다.")
                return True
            else:
                QMessageBox.warning(self, "오류", "데이터베이스 백업에 실패했습니다.")
                return False
        except Exception as e:
            QMessageBox.critical(self, "백업 오류", f"백업 실패: {str(e)}")
            return False

    def restore_database(self, backup_path):
        """데이터베이스 복원"""
        try:
            reply = QMessageBox.question(
                self, 
                "확인", 
                "데이터베이스를 복원하시겠습니까?\n현재 데이터가 모두 대체됩니다.",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                if self.db_manager.restore_database(backup_path):
                    self.load_data_from_db()  # 테이블 새로고침
                    QMessageBox.information(self, "완료", "데이터베이스 복원이 완료되었습니다.")
                    return True
                else:
                    QMessageBox.warning(self, "오류", "데이터베이스 복원에 실패했습니다.")
                    return False
        except Exception as e:
            QMessageBox.critical(self, "복원 오류", f"복원 실패: {str(e)}")
            return False

    # 데모용 메서드들 (SQLite 버전)
    def demo_add_data(self):
        """데모용 데이터 추가 예시"""
        try:
            # 새로운 데이터 추가
            self.db_manager.add_log_entry("192.168.1.100", "2025.01.07", "brute force", "Login attempt failed")
            self.db_manager.add_log_entry("10.0.0.50", "2025.01.07", "malware", "Suspicious file detected")
            
            # 테이블 새로고침
            self.load_data_from_db()
            
        except Exception as e:
            QMessageBox.critical(self, "오류", f"데모 데이터 추가 실패: {str(e)}")

    # 키보드 단축키 지원
    def keyPressEvent(self, event):
        """키보드 이벤트 처리"""
        if event.key() == Qt.Key.Key_Delete:
            self.delete_selected_logs()
        elif event.key() == Qt.Key.Key_A and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            # Ctrl+A로 모든 행 선택
            self.ui.tableWidget.selectAll()
        else:
            super().keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Page3()
    window.show()
    
    sys.exit(app.exec())