#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MB (1024 * 1024)

int main() {
    // حجم الفحص (ابدأ بـ 80 ميجا، لو علق صغّره لـ 40)
    size_t size_mb = 500;
    size_t size = size_mb * MB;
    unsigned char *buf = NULL;
    size_t i;
    size_t errors = 0;
    int rounds = 3;

    printf("=== فاحص ذاكرة بسيط ===\n");
    printf("الحجم: %zu ميجابايت | عدد الجولات: %d\n\n", size_mb, rounds);

    printf("جاري تخصيص الذاكرة...\n");
    buf = (unsigned char *)malloc(size);

    if (buf == NULL) {
        printf("[خطأ] فشل تخصيص الذاكرة!\n");
        printf("جرب تصغر الحجم (غير 80 إلى 40 أو 50)\n");
        return 1;
    }

    printf("[تم] تم تخصيص %zu ميجابايت بنجاح\n\n", size_mb);

    for (int r = 0; r < rounds; r++) {
        printf("الجولة %d من %d ... ", r + 1, rounds);

        // كتابة نمط في الذاكرة
        for (i = 0; i < size; i++) {
            buf[i] = (unsigned char)(i & 0xFF);
        }

        // قراءة والتحقق
        errors = 0;
        for (i = 0; i < size; i++) {
            if (buf[i] != (unsigned char)(i & 0xFF)) {
                errors++;
            }
        }

        if (errors == 0) {
            printf("سليمة\n");
        } else {
            printf("وجدت %zu خطأ!\n", errors);
        }
    }

    free(buf);

    printf("\n========================\n");
    if (errors == 0) {
        printf("النتيجة النهائية: الذاكرة سليمة في الجزء الذي تم فحصه\n");
    } else {
        printf("النتيجة النهائية: تم اكتشاف أخطاء في الذاكرة\n");
    }
    printf("========================\n");

    return 0;
}