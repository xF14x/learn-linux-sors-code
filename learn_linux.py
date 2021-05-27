
from config_app import *
# =-=-=-=-=-=-=-=-=-=
system("clear")
print(Fore.RED)
Write_Text_Animation(CopyRight)
sleep(2)
print(Fore.BLUE)
print(text_for_the_input)
while True:
    print(Fore.WHITE)
    Number_Of_The_Command = input(">>:")
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=
    print(Fore.GREEN)
    if Number_Of_The_Command == tou:
        print("""touch (إسم الملف.txt)

    . وإذا كنت تبي الملف يكون مخفي أكتب قبله إسمة
    نقطة

    وبس

    وخلها .txt وإذا تبيه بايثون نفس السالفة بس شيل
    .py

    وبس""")
    elif Number_Of_The_Command == mkdir:
        print("""عشان تسوي مجلد اكتب

    mkdir (إسم المجلد)

    . وإذا كنت تبيه يكون مخفي أكتب قبل الإسم
    نقطة

    وبس""")
    elif Number_Of_The_Command == nano:
        print("""أكتب nanoعشان تعدل النص ب

    nano (إسم الملف)

    وعشان تطلع
    control  + x

    y عشان تحفظ

    n عدم الحفظ

    contro + c للرجوع للنص""")
    elif Number_Of_The_Command == echo:
        print("""عشان تزيد على الملف كلام 

    echo إسم الملف<<  الكلام
    وبس""")
    elif Number_Of_The_Command == echo1:
        print("""عشان تسوي ملف  وتكتب فيه الكلام

    echo إسم الملف < الكلام
    وبس""")
    elif Number_Of_The_Command == cp:
        print("""عشان تنسخ اي ملف او مجلد

    cp (إسم الملف او المجلد) (الإسم الجديد) (اللوكيشن)

    وبس""")
    elif Number_Of_The_Command == mv:
        print("""كيف أنقل او أغير إسم الملف او المجلد

    mv  (إسم المجلد او الملف) (الإسم الجديد) (اللوكيشن إذا كنت تبي تنقلة)

    وبس""")
    elif Number_Of_The_Command == rm:
        print("""كيف أحذف الملف او المجلد

    إذا ملف

    rm (إسم المجلد)

    إذا مجلد

    rm -r (إسم المجلد)
    وبس""")
    elif Number_Of_The_Command == ls:
        print("""كيف أظهر اللي داخل الملف

    ls

    وإذا كنت تبي تشوف الملفات المخفية

    ls -a

    وإذا كنت تبي تشوف الملفات بس مرتبة ويطلعلك متا سويتها والساعة كم والخصائص الي فيها

    ls -l

    ويمديك تجمعهم كلهم

    ls -la
    وبس""")


    # =-=-=-=-=-=-=-=-=
    # Twitter
    elif Number_Of_The_Command == "T" or Number_Of_The_Command == "t":
        Open_Web(Twitter)
    # Youtube
    elif Number_Of_The_Command == "Y" or Number_Of_The_Command == "y":
        Open_Web(Youtube)
    # Github
    elif Number_Of_The_Command == "G" or Number_Of_The_Command == "g":
        Open_Web(GitHub)
    # Telegram
    elif Number_Of_The_Command == "Te" or Number_Of_The_Command == "te" or Number_Of_The_Command == "TE" or Number_Of_The_Command == "tE" :
        Open_Web(Telegram)
    # Exit
    elif Number_Of_The_Command == "x" or Number_Of_The_Command == "X" or Number_Of_The_Command == "exit" or Number_Of_The_Command == "Exit":
        print(Fore.WHITE)
        exit("Ok.")
    else:
        print(Fore.WHITE)
        print("Error")