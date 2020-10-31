# Перша програма у Python для об'єктивної оцінки своїх можливостей
# Гумор ради гумору

import time
import webbrowser
from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.CYAN, Style.BRIGHT)
print("# Перша програма у Python для об'єктивної оцінки своїх можливостей")
print("# Гумор ради гумору")

print(Fore.YELLOW, Style.BRIGHT)

name = input("Вкажіть Ваше імя: ")

try:
    C = int(input("Якої довжини Ваш Python: "))
except ValueError:
    print("Давайте заново,", name)
    C = 0
if 16 <= C <= 30:
    print("Маєте гарний скіл, козаче", name)
elif C > 30:
    print(name, ",пи#дите, як дишете")
else:
    print("Маловато буде,", name, "...")
    print("")
    time.sleep(2)
    webbrowser.open_new_tab('https://www.youtube.com/playlist?list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu')
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=fp5-XQFr_nk')
    webbrowser.open_new_tab('https://www.coursera.org/learn/mathematics-and-python')

time.sleep(4)
