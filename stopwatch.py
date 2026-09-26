import time

def stopwatch():
    seconds = 0
    
    while True:
        # 1. حساب الدقائق والثواني برياضيات بايثون
        minutes = seconds // 60  # القسمة بدون باقي تعطينا الدقائق
        display_seconds = seconds % 60  # باقي القسمة يعطينا الثواني
        
        # 2. طباعة الوقت بالشكل المفضل لديك (دقيقة : ثانية)
        print(f"Time => {minutes}:{display_seconds}")
        
        # 3. زيادة العداد ثانية واحدة والنوم
        seconds = seconds + 1
        time.sleep(1)
        
        # 4. شرط الأمان: كل 10 ثوانٍ مثلاً، سيسألك الكود هل تريد التوقف؟
        if seconds % 10 == 0:
            user_input = input("اضغط e للخروج، أو أي زر للاستمرار: ")
            if user_input == "e":
                print("تم إيقاف الساعة بنجاح!")
                break  # يكسر الحلقة ويوقف البرنامج

stopwatch()
