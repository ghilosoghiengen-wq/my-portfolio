#include <stdio.h>
#include <unistd.h> // مخصصة للـ Linux/Mac لعمل تأخير زمني، لـ Windows استخدم #include <windows.h>

#define WIDTH 60
#define HEIGHT 20

int main() {
    int x = 5, y = 5;   // مكان الكرة الإبتدائي
    int dx = 1, dy = 1; // اتجاه الحركة

    // كود ANSI لجعل النص باللون الأخضر وإخفاء المؤشر
    printf("\033[0;32m"); 
    printf("\033[?25l"); 

    while(1) {
        // تنظيف الشاشة
        printf("\033[H"); 

        // رسم اللوحة
        for (int i = 0; i < HEIGHT; i++) {
            for (int j = 0; j < WIDTH; j++) {
                if (i == 0 || i == HEIGHT - 1 || j == 0 || j == WIDTH - 1) {
                    printf("#"); // حدود الإطار
                } else if (i == y && j == x) {
                    printf("@"); // الكرة المتحركة (يمكنك تغييرها لـ 1 أو 0)
                } else {
                    printf(" "); // مسافة فارغة
                }
            }
            printf("\n");
        }

        // تحريك الكرة
        x += dx;
        y += dy;

        // الارتداد من الجدران
        if (x == 1 || x == WIDTH - 2) dx = -dx;
        if (y == 1 || y == HEIGHT - 2) dy = -dy;

        // تأخير زمني لضبط سرعة الأنميشن (بالمايكرو ثانية)
        usleep(50000); 
    }

    return 0;
}
