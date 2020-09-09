import  pyautogui as pq
import time as ti

print("# Зараз я хакну твій ноут")
ti.sleep(1)
print("3")
ti.sleep(1)
print("2")
ti.sleep(1)
print("1")

ti.sleep(2)
pq.hotkey("winleft")
ti.sleep(1)
pq.typewrite("chrome\n", 0.2)
ti.sleep(1)
pq.typewrite("https://www.youtube.com/watch?v=uc6f_2nPSX8\n",0.01)
ti.sleep(2)
pq.click(857,634,duration=0.1)
pq.click(857,634,duration=0.1)
ti.sleep(1)

