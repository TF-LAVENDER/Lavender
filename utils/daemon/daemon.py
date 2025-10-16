import threading
import time
import psutil
import logging
from typing import Optional, Callable
from datetime import datetime
import subprocess
import os
import csv
import re
from collections import defaultdict, deque


class ThreadDaemon:
    """
    간단한 스레드 기반 데몬 실행기.

    - start(): 데몬 스레드 시작 (이미 실행 중이면 무시)
    - stop(): 스레드에 정지 신호를 보내고 조인
    - set_task(task): 루프마다 실행할 콜러블 설정 (선택)
    - interval: 루프 간 대기 시간 초(기본 1.0)
    """

    def __init__(self, interval: float = 1.0, task: Optional[Callable[[], None]] = None) -> None:
        self._interval = interval
        self._task = task
        self._stop_event = threading.Event()
        self._thread: Optional[threading.Thread] = None

    def set_task(self, task: Callable[[], None]) -> None:
        self._task = task

    def _run(self) -> None:
        while not self._stop_event.is_set():
            try:
                if self._task is not None:
                    self._task()
            except Exception:
                # 실제 앱에서는 로깅으로 전환 가능
                pass
            finally:
                # stop 신호 확인을 위해 세분화된 sleep
                remaining = self._interval
                step = 0.05 if self._interval > 0.1 else self._interval
                while remaining > 0 and not self._stop_event.is_set():
                    time.sleep(min(step, remaining))
                    remaining -= step

    def start(self) -> None:
        if self._thread and self._thread.is_alive():
            return
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run, name="LavenderDaemon", daemon=True)
        self._thread.start()

    def stop(self, timeout: Optional[float] = 2.0) -> None:
        if not self._thread:
            return
        self._stop_event.set()
        self._thread.join(timeout=timeout)
        self._thread = None


def system_monitor_task():
    """
    시스템 모니터링 작업 함수
    - CPU 사용률, 메모리 사용률, 디스크 사용률 모니터링
    - 로그 파일에 기록 (선택적)
    """
    try:
        # CPU 사용률 (1초간 평균)
        cpu_percent = psutil.cpu_percent(interval=1)
        
        # 메모리 사용률
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        
        # 디스크 사용률
        disk = psutil.disk_usage('/')
        disk_percent = disk.percent
        
        # 현재 시간
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 콘솔에 출력 (실제 앱에서는 로그 파일이나 데이터베이스에 저장)
        print(f"[{current_time}] 시스템 상태 - CPU: {cpu_percent}%, 메모리: {memory_percent}%, 디스크: {disk_percent}%")
        
        # 특정 임계값 초과 시 경고
        if cpu_percent > 80:
            print(f"⚠️  경고: CPU 사용률이 높습니다 ({cpu_percent}%)")
        if memory_percent > 85:
            print(f"⚠️  경고: 메모리 사용률이 높습니다 ({memory_percent}%)")
        if disk_percent > 90:
            print(f"⚠️  경고: 디스크 사용률이 높습니다 ({disk_percent}%)")
            
    except Exception as e:
        print(f"시스템 모니터링 중 오류 발생: {e}")


def network_monitor_task():
    """
    네트워크 모니터링 작업 함수
    - 네트워크 인터페이스 상태 확인
    - 연결된 프로세스 모니터링
    """
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 네트워크 인터페이스 상태 (권한 문제와 무관하므로 별도 보호)
        try:
            net_io = psutil.net_io_counters()
            print(f"[{current_time}] 네트워크 - 송신: {net_io.bytes_sent} bytes, 수신: {net_io.bytes_recv} bytes")
        except Exception as counters_error:
            print(f"[{current_time}] 네트워크 카운터 조회 실패: {counters_error}")

    except Exception as e:
        # 여기까지 온 예외는 모두 삼키고 사용자에게만 알림
        print(f"네트워크 모니터링 중 오류 발생: {e}")


class NetworkAbuseWatcher:
    """
    네트워크 수신량이 임계치(KB/s) 이상으로 연속 지속될 때, 최다 수신 IP를 추정하여 차단 목록에 기록.

    - 샘플링 주기: tick() 호출 주기(권장 1초)
    - 임계치: threshold_kb_per_sec (기본 400000KB/s)
    - 지속 시간: sustain_seconds (기본 5초)
    """

    def __init__(self, threshold_kb_per_sec: int = 400000, sustain_seconds: int = 5) -> None:
        self.threshold_bytes_per_sec = threshold_kb_per_sec * 1024
        self.sustain_seconds = sustain_seconds
        self._prev_counters = None  # type: Optional[psutil._common.snetio]
        self._last_check_ts = None  # type: Optional[float]
        self._over_threshold_flags = deque(maxlen=sustain_seconds)
        self._cooldown_ips = {}  # ip -> last_added_ts
        self._cooldown_seconds = 300

    def _project_root(self) -> str:
        # utils/daemon/daemon.py -> 프로젝트 루트로 이동
        return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

    def _blocked_csv_path(self) -> str:
        # 절대 경로 /data 로 저장
        return "/data/blocked.csv"

    def _get_top_incoming_ip(self) -> Optional[str]:
        """
        macOS의 nettop 스냅샷을 1초 수집하여 bytes_in이 가장 큰 원격 IP를 추정.
        nettop이 없거나 파싱 실패 시 None 반환.
        """
        try:
            cmd = [
                "nettop", "-P", "-L", "1", "-x",
                "-J", "bytes_in,tcpsrc,udpsrc"
            ]
            proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
            if proc.returncode != 0:
                return None
            lines = proc.stdout.splitlines()
            bytes_in_by_ip = defaultdict(int)
            for line in lines:
                # 키=값 쌍 형태를 파싱
                # 예시: bytes_in=12345 tcpsrc=1.2.3.4:5678 ... 또는 udpsrc=...
                try:
                    pairs = dict(
                        part.split("=", 1) for part in line.split() if "=" in part
                    )
                except Exception:
                    continue
                ip_port = pairs.get("tcpsrc") or pairs.get("udpsrc")
                bytes_in_str = pairs.get("bytes_in")
                if not ip_port or not bytes_in_str:
                    continue
                # ip:port 에서 ip만 추출
                ip = ip_port.split(":")[0]
                try:
                    bytes_in = int(bytes_in_str)
                except ValueError:
                    continue
                bytes_in_by_ip[ip] += bytes_in

            if not bytes_in_by_ip:
                return None
            # 최다 수신 IP 반환
            return max(bytes_in_by_ip.items(), key=lambda kv: kv[1])[0]
        except FileNotFoundError:
            # nettop이 없는 환경
            return None
        except Exception:
            return None

    def _append_blocked_if_needed(self, ip: str) -> None:
        # 쿨다운 체크
        now = time.time()
        last_added = self._cooldown_ips.get(ip)
        if last_added and (now - last_added) < self._cooldown_seconds:
            return

        path = self._blocked_csv_path()
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # 중복 방지: 기존 CSV에 동일 IP 존재 여부 확인 (열 개수 4 또는 5 모두 허용)
        existing_ips = set()
        if os.path.exists(path):
            try:
                with open(path, mode="r", newline="", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if not row:
                            continue
                        # 5열: [idx, proto, port, ip, desc], 4열: [proto, port, ip, desc]
                        if len(row) >= 4:
                            existing_ips.add(row[-2])  # IP는 끝에서 두 번째 컬럼
            except Exception:
                pass

        if ip in existing_ips:
            self._cooldown_ips[ip] = now
            return

        # 4열 포맷으로 추가 (UI 로딩 시 인덱스 자동 부여)
        try:
            with open(path, mode="a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["ANY", "*", ip, "auto-blocked by daemon"])
            self._cooldown_ips[ip] = now
            print(f"자동 차단 등록: {ip} -> {path}")
        except Exception as e:
            print(f"blocked.csv 기록 실패: {e}")

    def tick(self) -> None:
        try:
            counters = psutil.net_io_counters()
            now = time.time()
            if self._prev_counters is None or self._last_check_ts is None:
                self._prev_counters = counters
                self._last_check_ts = now
                return

            elapsed = max(1e-6, now - self._last_check_ts)
            bytes_recv_delta = max(0, counters.bytes_recv - self._prev_counters.bytes_recv)
            rate_bps = bytes_recv_delta / elapsed
            over = rate_bps >= self.threshold_bytes_per_sec
            self._over_threshold_flags.append(over)

            # 상태 업데이트
            self._prev_counters = counters
            self._last_check_ts = now

            if len(self._over_threshold_flags) == self.sustain_seconds and all(self._over_threshold_flags):
                # 최다 수신 IP 추정 후 CSV 기록
                ip = self._get_top_incoming_ip()
                if ip:
                    self._append_blocked_if_needed(ip)
        except Exception as e:
            # 모니터링 실패는 로깅만 수행
            print(f"네트워크 수신량 감시 중 오류: {e}")


def application_health_check():
    """
    애플리케이션 상태 체크 함수
    - 메인 윈도우 상태 확인
    - 메모리 누수 체크
    - 성능 지표 수집
    """
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 현재 프로세스 정보
        process = psutil.Process()
        memory_info = process.memory_info()
        cpu_percent = process.cpu_percent()
        
        print(f"[{current_time}] 앱 상태 - 메모리: {memory_info.rss / 1024 / 1024:.1f}MB, CPU: {cpu_percent}%")
        
        # 메모리 사용량이 500MB 초과 시 경고
        if memory_info.rss / 1024 / 1024 > 500:
            print(f"⚠️  경고: 애플리케이션 메모리 사용량이 높습니다 ({memory_info.rss / 1024 / 1024:.1f}MB)")
            
    except Exception as e:
        print(f"애플리케이션 상태 체크 중 오류 발생: {e}")


def combined_monitoring_task():
    """
    통합 모니터링 작업 함수
    - 시스템, 네트워크, 애플리케이션 상태를 종합적으로 모니터링
    """
    print("=" * 50)
    print(f"데몬 모니터링 시작 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    system_monitor_task()
    network_monitor_task()
    application_health_check()
    
    print("=" * 50)


# 전역 싱글톤 인스턴스 (기본 작업 함수 설정)
daemon = ThreadDaemon(interval=5.0, task=combined_monitoring_task)

# 고수신량 감시 전용 데몬 (1초 주기)
_abuse_watcher = NetworkAbuseWatcher(threshold_kb_per_sec=400000, sustain_seconds=5)
network_daemon = ThreadDaemon(interval=1.0, task=_abuse_watcher.tick)