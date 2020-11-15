"_______________________________Цикли______________________________________________________________________________" """
for i in range (1,101):
    print(i, end="->")
else:
    print("End")

"--------------continue------------------"
while True:
    e = input("Введіть що-небудь: ")
    if e == "exit":
        break
    if len(e)<5:
        print("Мало!")
        continue                               # пропускає викоанання попередніх циклів
    print("Саме то!")}
     
   
"_______________________________Функції______________________________________________________________________________" 
def mi (x,y,z):
    res = x+y+z
    return  res
print(mi(1,1,1))
"--------------------------------" 
def jr (a,b):
    if a>b:
        print(a,"- max")
    elif a<b:
        print(b,"- max")
    else:
        print(a,"=",b)
jr(5,6)
x = 10; y = 6
jr(x,y)
"-------------global-------------------" 
X = 10
def GF():
    global X # резервуавння Х

    print ("X = ",X)
    X=45
    print("Заміна глобальне Х на локальне:",X)

GF()
print("Значення Х тепер = ",X) 
"----------func_key----------------------"
# Ключові параметри
def func(x,y,z):
    res = x**2+y**2+z**2
    print("x=",x,", y=",y,", z=",z)
    return res
print("x^2 + y^2 + z^2 = ",func(int(input("X = ")),int(input("Y = ")),int(input("Z = ")))) 
"----------function_varargs----------------------"
def total(a=5, *numbers, **phonebook): #* - кортеж, ** - словник
    print('a', a)

    # проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)

    # проход по всем элементам словаря
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560)) 
"----------keyword_only----------------------"
# Только ключевые параметры
def total (i = 5, *num, extra_num = 1): # Вказуєм початкові значення для extra_num
    c=i
    for n in num:
        c+= n
    c+= extra_num
    print(c)
total(10,1,2,3, extra_num = 10)
total(10,1,2,3)
"----------return----------------------"
# Замість запису print використовується return
def We(x,y):
    if x>y:
        return x
    elif x==y:
        return 'equal'
    else:
        return y
print(We(10,111))
"----------func_doc----------------------"
# Своєрідний запис замість print
def printMax (x,y):
    '''Выводит максимальное из двух чисел.
Оба значения должны быть целыми числами'''
    x = int (x)
    y = int (y)

    if x>y:
        print(x, "-Max")
    else:
        print(y, "-Max")
printMax(10,235)
print(printMax.__doc__)
"----------------------------------------------------------------------------------------------------------------------" 
def printMAX(x,y):
    '''
    Выводит максимальное из двух чисел.
    Оба значения должны быть целыми числами
    '''
    x = int(x)
    y = int(y)

    if x>y:
        print("Х - найбільша")
    else:
        print("У - найбільша")
print(printMAX.__doc__)
printMAX(input("X: "),input("Y: "))
"----------------------------------------модулі------------------------------------------------------------------------------" 
"-------------------using_sys---модулі-------------------"
# Вивід шляху файла коду
# Використання бібліотеки sys
import sys

print("Аргументи командної строки:")
for i in sys.argv:
    print(i)

print("\n\nЗмінна PythonPath має: ", sys.path, "\n")
"--------------імпорт усього із math---*----------------------------------------" 
from math import *
n = int(input("Введіть діапазон: "))
p = [2,3]
count = 2
a = 5
while (count<n):
    b = 0
    for i in range (2,a):
        if (i <= sqrt(a)):
            if (a % i == 0):
                print(a,"Непросте")
                b=1
            else:
                pass
    if (b != 1):
        print(a,"Просте")
        p+=[a]
    count+=1
    a+=2
print(p)
"---------------------------------------------------------" 
"----------using_name-----------"
#  __name___ - модуль запущений і готовий до роботи
if __name__ == '__main__':
    print("Програма запущена сама")
else:
    print("Імпортовано в інший модуль")

"------------DIR-----------------------" 
import sys
print(dir (sys))            # Виводить списки атрибутів модуля 'sys'
print(dir())                # Виводить списки атрибутів даного модуля
a = 5                       # Створюється змінна а
print(dir())                # Виводить списки атрибутів даного модуля з новою змінною 'а'
del a                       # Видаляється а
print(dir())                # Виводить списки атрибутів даного модуля же без

print(dir(int))             # Таким чином можна дізнатися про атрибути будь - якого модуля чи ф-ції
"""
