import sqlite3
import os
from datetime import datetime
from typing import List, Dict, Any, Optional
from models.blockedIp import BlockedIp

class DatabaseManager:
    def __init__(self, db_path: str = "blocked_ips.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """데이터베이스 초기화 및 테이블 생성"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS blocked_ips (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source_ip TEXT NOT NULL,
                    date TEXT NOT NULL,
                    event_type TEXT NOT NULL,
                    description TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_source_ip ON blocked_ips(source_ip)
            ''')
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_event_type ON blocked_ips(event_type)
            ''')
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_date ON blocked_ips(date)
            ''')
            
            conn.commit()
            
    def add_log_entry(self, ip: BlockedIp) -> int:
        """새로운 로그 엔트리 추가"""
        with sqlite3.connect(self.db_path) as conn: # TODO: sadasdasd
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO blocked_ips (source_ip, date, event_type, description)
                VALUES (?, ?, ?, ?)
            ''', (ip.ip, ip.date, ip.eventType, ip.description))
            conn.commit()
            return cursor.lastrowid
    
    def get_all_logs(self) -> List[Dict[str, Any]]:
        """모든 로그 엔트리 조회"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, source_ip, date, event_type, description, created_at
                FROM blocked_ips
                ORDER BY created_at DESC
            ''')
            return [dict(row) for row in cursor.fetchall()]
    
    def get_log_by_id(self, log_id: int) -> Optional[Dict[str, Any]]:
        """ID로 특정 로그 엔트리 조회"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, source_ip, date, event_type, description, created_at
                FROM blocked_ips
                WHERE id = ?
            ''', (log_id,))
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def update_log_entry(self, log_id: int, source_ip: str, date: str, event_type: str, description: str) -> bool:
        """로그 엔트리 업데이트"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE blocked_ips 
                SET source_ip = ?, date = ?, event_type = ?, description = ?
                WHERE id = ?
            ''', (source_ip, date, event_type, description, log_id))
            conn.commit()
            return cursor.rowcount > 0
    
    def delete_log_entry(self, log_id: int) -> bool:
        """로그 엔트리 삭제"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM blocked_ips WHERE id = ?', (log_id,))
            conn.commit()
            return cursor.rowcount > 0
    
    def search_logs(self, search_term: str = None, event_type: str = None, 
                   start_date: str = None, end_date: str = None) -> List[Dict[str, Any]]:
        """로그 검색"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            query = '''
                SELECT id, source_ip, date, event_type, description, created_at
                FROM blocked_ips
                WHERE 1=1
            '''
            params = []
            
            if search_term:
                query += ' AND (source_ip LIKE ? OR description LIKE ?)'
                params.extend([f'%{search_term}%', f'%{search_term}%'])
            
            if event_type:
                query += ' AND event_type = ?'
                params.append(event_type)
            
            if start_date:
                query += ' AND date >= ?'
                params.append(start_date)
            
            if end_date:
                query += ' AND date <= ?'
                params.append(end_date)
            
            query += ' ORDER BY created_at DESC'
            
            cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]
    
    def get_event_types(self) -> List[str]:
        """모든 이벤트 타입 조회"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT DISTINCT event_type FROM blocked_ips ORDER BY event_type')
            return [row[0] for row in cursor.fetchall()]
    
    def get_log_count(self) -> int:
        """총 로그 수 조회"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM blocked_ips')
            return cursor.fetchone()[0]
    
    def clear_all_logs(self) -> bool:
        """모든 로그 삭제"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM blocked_ips')
            conn.commit()
            return cursor.rowcount > 0
    
    def backup_database(self, backup_path: str) -> bool:
        """데이터베이스 백업"""
        try:
            with sqlite3.connect(self.db_path) as source:
                with sqlite3.connect(backup_path) as backup:
                    source.backup(backup)
            return True
        except Exception as e:
            print(f"백업 실패: {e}")
            return False
    
    def restore_database(self, backup_path: str) -> bool:
        """데이터베이스 복원"""
        try:
            if os.path.exists(backup_path):
                with sqlite3.connect(backup_path) as source:
                    with sqlite3.connect(self.db_path) as target:
                        source.backup(target)
                return True
            return False
        except Exception as e:
            print(f"복원 실패: {e}")
            return False