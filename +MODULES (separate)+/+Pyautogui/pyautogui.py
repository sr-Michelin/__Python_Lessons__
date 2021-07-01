import pyautogui as pq
import time as ti

'''pq.move(50,-50,0.5)                 # рухає курсором (незажатим)
pq.drag(50,50,0.5,button='left')       # рухає курсором (нажата ліва клавіша мишки)'''

'''print(pq.position())
pq.hotkey("winleft")                   # коварная фігня (не включати)
pq.click(32,990,duration=0.5)          # виключає ноут
pq.click(70,896,duration=0.5)
pq.click(70,896,duration=0.5)'''

'''pq.typewrite("'Hello World!'", 0.1) # записує введене речення у будь яке поле
pq.typewrite(["enter"])                # натискає вказану клавішу'''

'''
ti.sleep(2)
pq.hotkey("winleft")                   # The Emperor Protects
ti.sleep(1)
pq.typewrite("chrome\n", 0.2)
pq.hotkey("winleft"+"right")
pq.typewrite("https://youtu.be/zFSREjGbxEY\n",0.01)
'''

pq.alert("деяка інфа", "Головне повідомлення", button="Текст кнопки")
age = pq.prompt("Введіть свій вік", " Ваш вік")
print(age)  # Меню
pq.confirm("Вам вже є 18?", "Ви впевнені?", ("Так,є", "Ні, мене підставили!1!!1"))
pq.password("Введіть пароль", "Пароль")
pq.screenshot("yourPic.jpg")  # Скріншот
