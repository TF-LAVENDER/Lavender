import psutil
import time

def get_network_bytes():
    counters = psutil.net_io_counters()
    return counters.bytes_sent, counters.bytes_recv

print("실시간 네트워크 트래픽 모니터링 (Ctrl+C로 종료)")
prev_sent, prev_recv = get_network_bytes()

try:
    while True:
        time.sleep(1)
        sent, recv = get_network_bytes()
        sent_speed = sent - prev_sent
        recv_speed = recv - prev_recv
        print(f"↑ 보낸 속도: {sent_speed / 1024:.2f} KB/s ↓ 받은 속도: {recv_speed / 1024:.2f} KB/s")
        prev_sent, prev_recv = sent, recv
except KeyboardInterrupt:
    print("\n모니터링 종료")