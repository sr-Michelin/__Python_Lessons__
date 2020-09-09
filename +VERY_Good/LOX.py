import  pyautogui as pq
import time as ti

a=input("Якщо готові ризикнути усім, напишіть 'start': ")
if a=='start':
    print("Вимкнення компютера через:")
    print(3)
    ti.sleep(1)
    print(2)
    ti.sleep(1)
    print(1)
    pq.hotkey("winleft")
    pq.click(32,990,duration=0.5)
    pq.click(70,896,duration=0.5)
    pq.click(70,896,duration=0.5)
else:
    print("Ех...")
    ti.sleep(2)
