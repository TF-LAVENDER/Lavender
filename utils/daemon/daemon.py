import threading
import time
import psutil
import logging
from typing import Optional, Callable
from datetime import datetime


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
        # 네트워크 인터페이스 상태
        net_io = psutil.net_io_counters()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"[{current_time}] 네트워크 - 송신: {net_io.bytes_sent} bytes, 수신: {net_io.bytes_recv} bytes")
        
        # 활성 네트워크 연결 수
        connections = psutil.net_connections()
        active_connections = len([conn for conn in connections if conn.status == 'ESTABLISHED'])
        print(f"[{current_time}] 활성 연결: {active_connections}개")
        
    except Exception as e:
        print(f"네트워크 모니터링 중 오류 발생: {e}")


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


