import socket
import sys
from datetime import datetime

# إعداد الهدف ليكون الجهاز المحلي نفسه (أندرويد المستضيف)
target = "127.0.0.1"

print("=" * 60)
print(f"   Android Local Port Scanner v1.0 (Target: {target})   ")
print("=" * 60)
print(f"Scan started at: {str(datetime.now())}")

# قائمة بالمنافذ الشائعة في أندرويد والمحاكيات لفحصها بدقة
# 5555: ADB الافتراضي | 8080/8000: خوادم الويب للمحاكيات | 10000+: منافذ الخدمات الخلفية
common_ports = [80, 443, 1080, 3000, 5037, 5554, 5555, 8000, 8080, 9000, 9050, 9999]

# إضافة نطاق إضافي من المنافذ المخصصة للمحاكيات (من 8000 إلى 8100 ومن 5550 إلى 5560)
extended_ports = list(range(5550, 5560)) + list(range(8000, 8100))
ports_to_scan = sorted(list(set(common_ports + extended_ports)))

print(f"[*] Scanning {len(ports_to_scan)} high-risk local ports...")

found_open = False

try:
    for port in ports_to_scan:
        # إنشاء اتصال TCP فحص سريع (Timeout نصف ثانية)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        
        # محاولة الاتصال بالمنفذ
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"   [!!!] ALERT: Port {port} is OPEN on localhost!")
            found_open = True
            
            # محاولة بسيطة لمعرفة الخدمة التي تعمل على المنفذ (Banner Grabbing)
            try:
                s.send(b"Hello\r\n")
                banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                if banner:
                    print(f"         [i] Service Banner: {banner}")
            except:
                pass
        s.close()

except KeyboardInterrupt:
    print("\n[-] Scan interrupted by user.")
    sys.exit()

except socket.error:
    print("[-] Could not connect to the local network configuration.")
    sys.exit()

if not found_open:
    print("[+] All probed local ports are secured/closed.")
else:
    print("[*] Scan finished. Check open ports for potential IPC exploitation.")

