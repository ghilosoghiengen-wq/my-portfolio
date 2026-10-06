import os
import pwd

print("=" * 60)
print("   Android High-Privilege Process Hunter v1.0   ")
print("=" * 60)
print("[*] Scanning running processes for potential escalation vectors...")

# البحث في مجلدات العمليات النشطة
proc_path = "/proc"
found_targets = []

if os.path.exists(proc_path):
    for pid_dir in os.listdir(proc_path):
        # التأكد أن المجلد يحمل رقماً (أي أنه عملية نشطة)
        if pid_dir.isdigit():
            pid_full_path = os.path.join(proc_path, pid_dir)
            try:
                # معرفة صاحب العملية (UID)
                stat_info = os.stat(pid_full_path)
                uid = stat_info.st_uid
                
                # تصفية المعايير: نريد فقط العمليات التي تملكها الـ Root (0) أو System (1000)
                if uid == 0 or uid == 1000:
                    # فحص ما إذا كان مجلد صلاحيات هذه العملية (attr) متاحاً لنا للكتابة
                    attr_path = os.path.join(pid_full_path, "attr/current")
                    if os.path.exists(attr_path) and os.access(attr_path, os.W_OK):
                        
                        # محاولة قراءة اسم البرنامج (Process Name)
                        cmdline_path = os.path.join(pid_full_path, "cmdline")
                        proc_name = "Unknown"
                        if os.path.exists(cmdline_path):
                            with open(cmdline_path, "r") as f:
                                proc_name = f.read().replace('\x00', ' ').strip()
                        
                        print(f"   [!!!] TARGET FOUND: PID {pid_dir} ({proc_name})")
                        print(f"         Owner UID: {uid} | Vulnerable Path: {attr_path}")
                        found_targets.append(pid_dir)
            except:
                continue

if not found_targets:
    print("[+] No dangerous root/system processes are leaking permissions locally.")
else:
    print(f"\n[*] Scan complete. Found {len(found_targets)} targets.")
    print("[*] Professional Tip: You can now monitor the target PID using: strace -p [PID]")

