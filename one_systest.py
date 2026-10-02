import os
import sys

def print_banner():
    print("=" * 60)
    print("   Android Root Finder & Binaries Scanner v1.2   ")
    print("=" * 60)

def search_hidden_su_binaries():
    print("\n[*] 1. Searching for Hidden or Leaked SU Binaries...")
    # مسارات عميقة يبحث فيها الهاكرز عن مخلفات الروت أو ملفات su منسية
    suspect_paths = [
        "/system/bin/su", "/system/xbin/su", "/sbin/su", "/su/bin/su",
        "/system/sd/xbin/su", "/system/bin/failsafe/su", "/data/local/xbin/su",
        "/data/local/bin/su", "/data/local/tmp/su", "/data/local/tmp/daemonsu"
    ]
    
    found = False
    for path in suspect_paths:
        if os.path.exists(path):
            print(f"   [!!!] Found SU Binary: {path}")
            # التحقق من صلاحيات التشغيل
            if os.access(path, os.X_OK):
                print(f"   [+] Executable SU found at: {path}")
            found = True
            
    if not found:
        print("[+] No standard hidden SU binaries found.")

def audit_tmp_folder():
    print("\n[*] 2. Deep Auditing '/data/local/tmp' for Executable Exploits...")
    # مجلد tmp هو البيئة المفضلة لحقن الملفات التنفيذية
    tmp_path = "/data/local/tmp"
    if os.path.exists(tmp_path):
        try:
            files = os.listdir(tmp_path)
            if not files:
                print("[+] /data/local/tmp is empty and clean.")
            for file in files:
                full_path = os.path.join(tmp_path, file)
                stat_info = os.stat(full_path)
                # فحص لو كان الملف يمتلك صلاحيات تنفيذ أو صلاحيات SUID
                if os.access(full_path, os.X_OK):
                    print(f"   [i] Found Executable File in Tmp: {full_path} (UID: {stat_info.st_uid})")
        except Exception as e:
            print(f"[-] Cannot read /data/local/tmp: {e}")
    else:
        print("[-] /data/local/tmp path not accessible.")

if __name__ == "__main__":
    print_banner()
    search_hidden_su_binaries()
    audit_tmp_folder()
    print("\n[*] Audit complete.")

