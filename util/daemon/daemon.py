import threading
import time
import psutil
import logging
import subprocess
import re
from typing import Optional, Callable, Dict, List, Set
from datetime import datetime
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


def get_arp_table():
    """
    시스템 ARP 테이블을 읽어서 반환
    """
    try:
        # macOS/Linux에서 arp 명령어 실행
        result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"ARP 테이블 조회 실패: {result.stderr}")
            return {}
        
        arp_table = {}
        lines = result.stdout.strip().split('\n')
        
        for line in lines:
            # ARP 테이블 파싱 (형식: hostname (192.168.1.1) at aa:bb:cc:dd:ee:ff [ether] on en0)
            match = re.search(r'\((\d+\.\d+\.\d+\.\d+)\)\s+at\s+([a-fA-F0-9:]{17})', line)
            if match:
                ip = match.group(1)
                mac = match.group(2).upper()
                arp_table[ip] = mac
                
        return arp_table
        
    except Exception as e:
        print(f"ARP 테이블 조회 중 오류: {e}")
        return {}


# 전역 변수: ARP 모니터링용
arp_history = defaultdict(lambda: deque(maxlen=10))  # 각 IP별 최근 10개 MAC 주소 기록
suspicious_ips = set()  # 의심스러운 IP 목록
blocked_ips = set()     # 차단된 IP 목록
page3_instance = None   # Page3 인스턴스 참조 (로그 연동용)


def analyze_arp_patterns(current_arp_table: Dict[str, str]) -> List[str]:
    """
    ARP 패턴을 분석하여 의심스러운 IP들을 반환
    """
    suspicious = []
    
    for ip, mac in current_arp_table.items():
        # IP별 MAC 주소 히스토리 업데이트
        if ip in arp_history:
            arp_history[ip].append(mac)
        else:
            arp_history[ip] = deque([mac], maxlen=10)
        
        # 의심스러운 패턴 분석
        mac_history = list(arp_history[ip])
        
        # 1. 동일 IP에 여러 MAC 주소가 할당된 경우
        unique_macs = set(mac_history)
        if len(unique_macs) > 1:
            if ip not in suspicious_ips:
                suspicious.append(ip)
                suspicious_ips.add(ip)
                print(f"🚨 ARP Spoofing 탐지: {ip}에 {len(unique_macs)}개의 서로 다른 MAC 주소 발견")
                print(f"   MAC 주소들: {', '.join(unique_macs)}")
        
        # 2. 게이트웨이 IP (보통 .1로 끝남)의 MAC 주소 변경
        if ip.endswith('.1') and len(mac_history) > 1:
            if ip not in suspicious_ips:
                suspicious.append(ip)
                suspicious_ips.add(ip)
                print(f"🚨 Gateway Spoofing 탐지: 게이트웨이 {ip}의 MAC 주소 변경")
    
    return suspicious


def auto_block_suspicious_ip(ip: str):
    """
    의심스러운 IP를 자동으로 차단
    """
    try:
        if ip in blocked_ips:
            return  # 이미 차단된 IP
        
        # macOS 방화벽으로 차단
        subprocess.run([
            'sudo', 'pfctl', '-t', 'blocked_ips', '-T', 'add', ip
        ], check=True)
        
        # pfctl 규칙 파일에 차단 규칙 추가
        block_rule = f"block in from {ip} to any\n"
        
        with open('/tmp/netchury_blocked_ips.pf', 'a') as f:
            f.write(block_rule)
        
        subprocess.run([
            'sudo', 'pfctl', '-f', '/tmp/netchury_blocked_ips.pf',
            '-a', 'netchury_blocked', '-e'
        ], check=True)
        
        blocked_ips.add(ip)
        print(f"🛡️  자동 차단: {ip}을(를) 방화벽에서 차단했습니다")
        
    except subprocess.CalledProcessError as e:
        print(f"IP 차단 실패 ({ip}): {e}")
    except Exception as e:
        print(f"IP 차단 중 오류 ({ip}): {e}")


def arp_spoofing_monitor():
    """
    ARP spoofing 탐지 및 차단 모니터링
    """
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # ARP 테이블 조회
        arp_table = get_arp_table()
        
        if not arp_table:
            return
        
        # 의심스러운 패턴 분석
        suspicious_ips_detected = analyze_arp_patterns(arp_table)
        
        # 의심스러운 IP 자동 차단
        for ip in suspicious_ips_detected:
            auto_block_suspicious_ip(ip)
            
            # 로그 이벤트 생성 (Page3와 연동 가능)
            log_arp_event(ip, arp_table.get(ip, "Unknown"))
        
        # 상태 출력
        if suspicious_ips_detected:
            print(f"[{current_time}] ARP 모니터링 - {len(suspicious_ips_detected)}개 의심 IP 탐지")
        else:
            print(f"[{current_time}] ARP 모니터링 - 정상")
            
    except Exception as e:
        print(f"ARP spoofing 모니터링 중 오류: {e}")


def log_arp_event(ip: str, mac: str):
    """
    ARP spoofing 이벤트를 로그에 기록 (Page3와 연동)
    """
    try:
        # Page3 로그 시스템과 연동할 수 있도록 이벤트 생성
        event_data = {
            'type': 'ARP_SPOOFING',
            'ip': ip,
            'mac': mac,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'description': f'의심스러운 ARP 활동 감지 - IP: {ip}, MAC: {mac}'
        }
        
        # 콘솔에 로그 출력
        print(f"📝 보안 로그: {event_data['description']}")
        
        # Page3 인스턴스와 연동하여 실제 로그 테이블에 추가
        if page3_instance:
            try:
                page3_instance.add_log_entry([
                    "ARP_SPOOFING", ip, "", "0.0.0.0", "0", 
                    f"의심스러운 ARP 활동 - MAC: {mac}"
                ])
            except Exception as e:
                print(f"Page3 로그 연동 실패: {e}")
        
    except Exception as e:
        print(f"ARP 이벤트 로깅 중 오류: {e}")


def combined_monitoring_task():
    """
    통합 모니터링 작업 함수
    - 시스템, 네트워크, 애플리케이션 상태를 종합적으로 모니터링
    - ARP spoofing 탐지 및 차단
    """
    print("=" * 50)
    print(f"데몬 모니터링 시작 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    system_monitor_task()
    network_monitor_task()
    application_health_check()
    
    # ARP spoofing 모니터링 (보안 강화)
    arp_spoofing_monitor()
    
    print("=" * 50)


# 전역 싱글톤 인스턴스 (기본 작업 함수 설정)
daemon = ThreadDaemon(interval=5.0, task=combined_monitoring_task)