#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define WIDTH 60
#define HEIGHT 20

int main() {
    int drops[WIDTH];

    // تهيئة أماكن القطرات بشكل عشوائي في الأعلى
    for (int i = 0; i < WIDTH; i++) {
        drops[i] = rand() % HEIGHT;
    }

    // إخفاء المؤشر وجعل النص باللون الأخضر
    printf("\033[?25l");
    printf("\033[0;32m"); 

    while (1) {
        // تنظيف الشاشة والعودة للبداية
        printf("\033[H");

        for (int y = 0; y < HEIGHT; y++) {
            for (int x = 0; x < WIDTH; x++) {
                // إذا كانت القطرة في هذا الموقع، نطبع رقم عشوائي
                if (drops[x] == y) {
                    printf("%d", rand() % 2); // يطبع 0 أو 1
                } else {
                    printf(" "); // مسافة فارغة لتمثيل الفراغ الأسود
                }
            }
            printf("\n");
        }

        // تحريك القطرات للأسفل
        for (int i = 0; i < WIDTH; i++) {
            drops[i]++;
            // إذا وصلت القطرة للنهاية، تعود للأعلى بشكل عشوائي
            if (drops[i] >= HEIGHT) {
                if (rand() % 10 > 7) { 
                    drops[i] = 0;
                } else {
                    drops[i] = -1; // تأخير ظهورها قليلاً
                }
            }
        }

        // سرعة تساقط المطر (بالمايكرو ثانية)
        usleep(50000); 
    }

    return 0;
}
