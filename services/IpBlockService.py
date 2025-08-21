
import subprocess
import os
import platform
import tempfile

DB_PATH = "blocked_ips.db"

class IpBlockService:
    def __init__(self):
        os = platform.system()
    
  # 차단
    def block_ip(self, ip):
        if self.os == "Linux":
            return self._block_ip_linux(ip)
        elif self.os == "Windows":
            return self._block_ip_windows(ip)
        elif self.os == "Darwin":  # macOS
            return self._block_ip_mac(ip)
        else:
            print(f"[!] 지원하지 않는 운영체제입니다: {self.os}")
            return False

    def _block_ip_linux(self, ip):
        try:
            subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
            print(f"[+] Linux: IP {ip} 차단 완료")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[!] Linux: IP 차단 실패: {ip}, 오류: {e}")
            return False

    def _block_ip_windows(self, ip):
        try:
            subprocess.run([
                "netsh", "advfirewall", "firewall", "add", "rule",
                f"name=Block {ip}", "dir=in", "action=block", f"remoteip={ip}"
            ], check=True)
            print(f"[+] Windows: IP {ip} 차단 완료")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[!] Windows: IP 차단 실패: {ip}, 오류: {e}")
            return False

    def _block_ip_mac(self, ip):
        success = self._block_ip_mac_pfctl(ip)
        if success:
            print(f"[+] Mac: Ip {ip} 차단 완료")
            return True
        else:
            print(f"[!] Mac: Ip {ip} 차단 실패")

    def _block_ip_mac_pfctl(self, ip):
        """
        pfctl을 사용한 IP 차단 (macOS 권장 방법)
        """
        try:
            # pf 규칙 파일 생성
            pf_rule = f"block drop from {ip} to any\n"
            
            # 임시 파일에 규칙 작성
            with tempfile.NamedTemporaryFile(mode='w', suffix='.pf', delete=False) as f:
                f.write(pf_rule)
                temp_file = f.name
            
            try:
                # pfctl로 규칙 적용
                subprocess.run([
                    "sudo", "pfctl", "-f", temp_file
                ], check=True, capture_output=True)
                
                # pf 활성화
                subprocess.run([
                    "sudo", "pfctl", "-e"
                ], check=True, capture_output=True)
                
                print(f"[+] macOS (pfctl): IP {ip} 차단 완료")
                return True
                
            finally:
                # 임시 파일 정리
                os.unlink(temp_file)
                
        except subprocess.CalledProcessError as e:
            print(f"[!] macOS (pfctl): IP 차단 실패: {ip}, 오류: {e}")
            return False
        except Exception as e:
            print(f"[!] macOS (pfctl): 예상치 못한 오류: {e}")
            return False
        
# 차단 해제

    def unblock_ip(self, ip):
        """통합 차단 해제 메서드"""
        if self.os == "Linux":
            return self._unblock_ip_linux(ip)
        elif self.os == "Windows":
            return self._unblock_ip_windows(ip)
        elif self.os == "Darwin":  # macOS
            return self._unblock_ip_mac(ip)
        else:
            print(f"[!] 지원하지 않는 운영체제입니다: {self.os}")
            return False

    def _unblock_ip_linux(self, ip):
        """Linux용 IP 차단 해제 (iptables 사용)"""
        try:
            subprocess.run(["sudo", "iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"], check=True)
            print(f"[+] Linux: IP {ip} 차단 해제 완료")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[!] Linux: IP 차단 해제 실패: {ip}, 오류: {e}")
            return False

    def _unblock_ip_windows(self, ip):
        """Windows용 IP 차단 해제 (netsh 사용)"""
        try:
            subprocess.run([
                "netsh", "advfirewall", "firewall", "delete", "rule",
                f"name=Block {ip}", "dir=in"
            ], check=True)
            print(f"[+] Windows: IP {ip} 차단 해제 완료")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[!] Windows: IP 차단 해제 실패: {ip}, 오류: {e}")
            return False

    def _unblock_ip_mac(self, ip):
        """Mac용 IP 차단 해제 (pfctl 사용)"""
        success = self._unblock_ip_mac_pfctl(ip)
        if success:
            print(f"[+] Mac: IP {ip} 차단 해제 완료")
            return True
        else:
            print(f"[!] Mac: IP {ip} 차단 해제 실패")
            return False

    def _unblock_ip_mac_pfctl(self, ip):
        """Mac pfctl을 사용한 실제 차단 해제 로직"""
        try:
            # pfctl 테이블에서 IP 제거
            subprocess.run([
                "sudo", "pfctl", "-t", "blocked_ips", "-T", "delete", ip
            ], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"[!] Mac pfctl 차단 해제 실패: {ip}, 오류: {e}")
            return False