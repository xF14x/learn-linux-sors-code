from colorama import Fore, Back, Style
from os import system
from webbrowser import open as Open_Web
# =-=-=-=-=-=-=-=-=-=
system("clear")
print(Fore.RED)
print("""
  _                         _ _                  
 | | ___  __ _ _ __ _ __   | (_)_ __  _   ___  __
 | |/ _ \/ _` | '__| '_ \  | | | '_ \| | | \ \/ / github(xF14x)
 | |  __/ (_| | |  | | | | | | | | | | |_| |>  <  twitter:(F14Commander)
 |_|\___|\__,_|_|  |_| |_| |_|_|_| |_|\__,_/_/\_\ youtube:(F14Commander سليمان المهوس)
""")
print(Fore.BLUE)
tou = "1"
mkdir = "2"
nano = "3"
echo = "4"
echo1 = "5"
cp = "6"
mv = "7"
rm = "8"
ls = "9"
Twitter = "https://twitter.com/F14Commander"
Youtube = "https://www.youtube.com/channel/UCcOXGSw12Y-d4359PWLrxgQ"
GitHub = "https://github.com/xF14x"
Telegram = "https://t.me/F14CommanderTech"
print("""
(1) كيف تسوي ملف

(2) كيف تسوي مجلد

(3) nano كيف تعدل ب

(4) echo كيف تزيد كلام ب

(5) echo كيف تسوي ملف ب

(6) كيف تنسخ ملف او مجلد

(7) كيف تنقل او تغير إسم ملف او مجلد

(8) كيف تحذف ملف او مجلد

(9) كيف تظهر الي داخل الملف

(T) حسابي في تويتر 

(Y) قناتي على اليوتيوب
""")
print(Fore.WHITE)
Number_Of_The_Command = input("??:")
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
if Number_Of_The_Command == mkdir:
    print("""عشان تسوي مجلد اكتب

mkdir (إسم المجلد)

. وإذا كنت تبيه يكون مخفي أكتب قبل الإسم
نقطة

وبس""")
if Number_Of_The_Command == nano:
    print("""أكتب nanoعشان تعدل النص ب

nano (إسم الملف)

وعشان تطلع
control  + x

y عشان تحفظ

n عدم الحفظ

contro + c للرجوع للنص""")
if Number_Of_The_Command == echo:
    print("""عشان تزيد على الملف كلام 

echo إسم الملف<<  الكلام
وبس""")
if Number_Of_The_Command == echo1:
    print("""عشان تسوي ملف  وتكتب فيه الكلام

echo إسم الملف < الكلام
وبس""")
if Number_Of_The_Command == cp:
    print("""عشان تنسخ اي ملف او مجلد

cp (إسم الملف او المجلد) (الإسم الجديد) (اللوكيشن)

وبس""")
if Number_Of_The_Command == mv:
    print("""كيف أنقل او أغير إسم الملف او المجلد

mv  (إسم المجلد او الملف) (الإسم الجديد) (اللوكيشن إذا كنت تبي تنقلة)

وبس""")
if Number_Of_The_Command == rm:
    print("""كيف أحذف الملف او المجلد

إذا ملف

rm (إسم المجلد)

إذا مجلد

rm -r (إسم المجلد)
وبس""")
if Number_Of_The_Command == ls:
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
if Number_Of_The_Command == "T" or Number_Of_The_Command == "t":
    Open_Web(Twitter)
# Youtube
if Number_Of_The_Command == "Y" or Number_Of_The_Command == "y":
    Open_Web(Youtube)
# Github
if Number_Of_The_Command == "G" or Number_Of_The_Command == "g":
    Open_Web(GitHub)
# Telegram
if Number_Of_The_Command == "Te" or Number_Of_The_Command == "te" or Number_Of_The_Command == "TE" or Number_Of_The_Command == "tE" :
    Open_Web(Telegram)
