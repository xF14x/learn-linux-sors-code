from colorama import Fore, Back, Style
from os import system
import sys
from time import sleep
from webbrowser import open as Open_Web

text_for_the_input = """
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

(G) Github حسابي في 

(TE) قناتي بالتيليقرام
"""

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

CopyRight = """
  _                         _ _                  
 | | ___  __ _ _ __ _ __   | (_)_ __  _   ___  __
 | |/ _ \/ _` | '__| '_ \  | | | '_ \| | | \ \/ / github(xF14x)
 | |  __/ (_| | |  | | | | | | | | | | |_| |>  <  twitter:(F14Commander)
 |_|\___|\__,_|_|  |_| |_| |_|_|_| |_|\__,_/_/\_\ youtube:(F14Commander سليمان المهوس)
"""




def Write_Text_Animation(Message):
    for char in Message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char !="\n":
            sleep(0.01)
        else:
            sleep(0.01)