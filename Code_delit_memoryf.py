# هذه هي الذاكرة التخيلية الخاصة بنا (تبدأ فارغة)
virtual_memory = {}


# دالة حجز مكان في الذاكرة وتخزين قيمة فيه
def malloc(variable_name, value):
    virtual_memory[variable_name] = value
    print(f"🔄 تم حجز مكان للمتغير '{variable_name}' في الذاكرة.")


# دالة مسح الذاكرة بالكامل عند الخروج
def free():
    # نستخدم دالة clear لتنظيف الذاكرة تماماً
    virtual_memory.clear()
    print("🧹 تم تنظيف الذاكرة بالكامل بنجاح!")


# --- تجربة الكود ---

# 1. نحجز متغيرات (مثل malloc في السي)
malloc("w", 150)
malloc("x", 45)

# لنرى شكل الذاكرة الآن
print("الذاكرة الحالية:", virtual_memory)

# 2. عند الخروج، نمسح كل شيء
free()

# لنرى الذاكرة بعد التنظيف
print("الذاكرة بعد free:", virtual_memory)
