import sqlite3
import time
from IpBlockService import IpBlockService
import os
import sys
import signal

DB_PATH = "blocked_ips.db"  # SQLite DB 경로
CHECK_INTERVAL = 60  # 초 단위로 DB를 체크하는 주기

BLOCKED_IPS = set()

def get_blocklist_from_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT source_ip FROM blocked_ips")  # 테이블 이름 및 컬럼명 확인 필요
        results = cursor.fetchall()
        conn.close()
        return {row[0] for row in results}
    except Exception as e:
        print(f"[ERROR] DB 접속 실패: {e}")
        return set()

def block_ip(ip):
    if ip not in BLOCKED_IPS:
        try:
            IpBlockService.block_ip(ip)
            print(f"[INFO] 차단된 IP: {ip}")
            BLOCKED_IPS.add(ip)
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] iptables 실패: {e}")

def unblock_removed_ips(current_ips):
    to_unblock = BLOCKED_IPS - current_ips
    for ip in to_unblock:
        try:
            IpBlockService.unblock_ip(ip)
            print(f"[INFO] 차단 해제된 IP: {ip}")
            BLOCKED_IPS.remove(ip)
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] iptables 해제 실패: {e}")

def main():
    print("[INFO] IP 차단 데몬 시작")

    def handle_sigterm(signum, frame):
        print("\n[INFO] 종료 시그널 수신. 정리 후 종료.")
        sys.exit(0)

    signal.signal(signal.SIGTERM, handle_sigterm)

    while True:
        current_ips = get_blocklist_from_db()
        for ip in current_ips:
            block_ip(ip)
        unblock_removed_ips(current_ips)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
        main()
