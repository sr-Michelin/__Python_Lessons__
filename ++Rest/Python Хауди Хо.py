'====================================================' '''
# Екранування \" \"   '""'
print("123 \"1234\" 1234 12")
print('123  "1234"  1234 12')

# Переведеня строки \n
print('Help\nme ')

# Додавання строк '+'
# поліморфізм -- додавання строк print (vlad.name + " " + str(vlad.age))
m='Міша'
n = 22
print('Я ' + m + ',і мені ' + str(n)+ ' рочки') # у випадку додавання чисел до строк використовуєм str(Num)

# Алгебра
a = 1
print("Табличка степенів")
try:
    n = int(input("Введіть кількість елеметів: "))
except ValueError:
    print("Введений знак не є цифрою")
    n = 0
print("Ви отрмаєте ",n,"елементів у",n,"-й степені" )

for i in range(n):
    b = a ** n
    print(a,'',b)
    a += 1

# Унарний мінус - міняє знак числа
a = 10
a = -a
print(a)

# Заокруглення
a = 10.556
print(round(a))
# або
import math
print(math.floor(a))   # в меншу сторону
print(math.ceil(a))    # в більшу сторону

# 'Дебільний' калькулятор
what = input("Що робим? (+,-): ")

a = int(input("Введи перше число:"))
b = int(input("Введи друге число:"))

if what == "+":
    c = a + b
    print("Результат:",c)
elif what == "-":
    c = a - b
    print("Результат:", c)
else:
    print("Вибрана неправильна операція!") 

# Колір тексту
from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.LIGHTRED_EX)
print(Style.BRIGHT)
print("Hello World!")

'''
# Створення exe-шника
'pyinstaller -F test.py'
# Погода
