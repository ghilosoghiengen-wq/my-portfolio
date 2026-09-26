# هنا تسأل الشخص الوهمي (الروبوت) عن اسمه أولاً
name = input("What's your name?\n")
print(f"Hello %s, I am glad to meet you!" % name)

# هنا الشخص الوهمي يسألك أنت عن اسمك
my_name = input(f"And what's your name?\n")
print(f"Hello {my_name}! My name is {name}, nice to talk to you.")

# يبدأ الحوار حول الحال، والشخص الوهمي يذكر اسمك
wgg = input(f"كيف هو حالك يا {my_name}؟\n")

if wgg == "حالي جيد" or wgg == "انا بخير":
    # هنا الروبوت يرد ويذكر اسمه في نهاية الجملة للتأكيد
    print(f"جيد لأنك بخير! معك صديقك {name}.")
    
    # استمرار الحوار مع ذكر الاسماء
    reply = input(f"هل تريد أن نحكي في شيء آخر يا {my_name}؟\n")
    if reply == "شكرا لأنك تسأل عني" or reply == "لا شكرا":
        print(f"العفو يا {my_name}، هذا واجبي أنا {name} كصديق لك!")
    else:
        print(f"أتمنى لك يوماً سعيداً يا {my_name}!")

elif wgg == "حالي جيد لكن لما تسأل" or wgg == "انا بخير حالي جيد لكن لما تسأل":
    print(f"أسأل لأنك صديقي يا {my_name}، وأنا {name} أهتم بأصدقائي.")
    
    reply = input("هل أعجبك اهتمامي؟ (نعم / لا)\n")
    if reply == "نعم" or reply == "شكرا لأنك تسأل عني":
        print(f"الأصدقاء دائماً يهتمون ببعضهم! يسعدني هذا يا {my_name}. ❤️")
    else:
        print(f"على الرحب والسعة على أي حال يا {my_name}.")

else:
    print(f"ولما حالك سيء يا {my_name}؟ أخبر صديقك {name}.")
    
    reason = input("هل تريد أن تخبرني بالسبب؟\n")
    print(f"لا تقلق يا {my_name}، كل شيء سيكون على ما يرام، صديقك {name} هنا لأجلك.")
