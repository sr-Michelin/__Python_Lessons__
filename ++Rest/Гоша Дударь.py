"""
# Все ради KSP та #####
print("Hello,KSP RSS RP-0")
print ("")
"--------------------------if-------------------------------"
# Перша програма у Python для об'єктивної оцінки своїх можливостей
# Вже не бракує except
# Гумор ради гумору
name = input("Вкажіть своє імя: ")
try:
    C = int(input("Скільки см має твій Python: "))
except ValueError:
    print("Давай по новой,",name)
    C = 0
if C >= 15 and C <= 30:
    print("Маєш гарний х#й, козаче",name)
elif C > 30:
    print(name,",пи#диш, як дишеш")
else:
    print("Маловато буде,",name,"...")
"--------------------------format----------------------------------------"
# Запис змінинних через format ()
age = 22        # {0}
name = "Mike"   # {1}
print('Возраст {0} -- {1} лет.'.format(name, age))
print('Почему {0} забавляется со своим Python?'.format(name))

print('{0:.3}'.format(0.33333)) # запис з певною точністю після коми
"------------------while not ---if---------else--------------------"
# Використання циклів у задачці, яка зрівнює один з одним два рондомні введені чила
print ("")
num_1 = float(input ("Введіть А: "))
num_2 = float(input ("Введіть В: "))
while not  num_1==num_2:
    if num_1>num_2:
        num_1-=1
        num_3=num_1-num_2
        print(num_1, num_2, num_3)
    elif num_1<num_2:
        num_1+=1
        num_3 = num_2 - num_1
        print(num_1, num_2, num_3)
else:
        print("A=B")
"----------------while not----------------------------------"
# Виведення числа до шуканого черз цикл (єб#та якась)
Num_1=int(input("Введіть будь-яке число:"))
while not Num_1==1000:
    Num_1+=1
    print(Num_1)
"------------Test---------------------------------------"
# Прога для перемноження введеного знаку на введене число (єб#та якась)
Test=input("Write smth:")
n=int(input("Write n: "))
Test *=n
print(Test)  j h
"-------------if--------------------------------------------"
# (єб#та якась)
name = input("Введіть слово: ")
A = 'Yes' if name == "Mike" else 'No'
print(A)
"-----------------for------------------------------------"
# Запис "Hello World" з подвоєнням кожної літери (єб#та якась)
for j in "Hello World":
    print(j*2, end="")7
"---------------continue---------------------------"
# Оператор continue який пропускає одну ітерацію у циклі
for j in "Hello World":
    if j == "W":
        continue
    print(j*3, end="")
"---------------break---------------------------"
# Якщо введена літера міститься у "Hello World", цикл зупиняється
# В іншому випадку отримаєм подвоєнні літери
n = input("Введіть літеру латинського алфавіту: ")
for j in "Hello World":
    if j == n:
        break
    print(j*2, end="")
else:
    print("")
"---------------list---------------------------------------------------------------------------------------------------"
# Робота із списками
# Структура впорядкованого набору даних [певна послідовність]
lis = [input("Заповніть список: ")]
liss = [1,2,6,4]
print(lis,liss)
"---------list------append---extend---insert---remove---count---pop----sort----reverse------clear---1"
l1=[1]
l2=[3,4,5]
l3=["M","i","k","e","S","h","e","v","c","h","e","n","k","o"]
l1.append(2)             #додає елемент в кінець списку
l1.extend(l2)            #додає
l1.insert(1,"Mike")      #замінює
l2.remove(5)             #видаляє
print(l3.count("M"))
print(l2.pop(0))         #видаляє вказаний елемент
print(l1)
l3.sort()                #сортує за параметром
print(l3)
l3.reverse()             #перевертає список
print(l3)
l3.clear()               #очищує
print(l3)

"---------------list---------------------------2"
# приклад пошуку у списку і переліку за типом
l4 = [input("Заповніть список: ")]
n = input("Виберіть шуканий знак: ")
print("Знайдено знаків",n,": ",l4.count(n))
"---------------list---------------------------3"
# вибірка за індексом
l5 = [1,2,3,4,5,6,7,8,9,0]
print(l5[0],l5[-1])       # тут l5[-1] відображає останій (-1) елемент
"---------------list---------------------------4"
# приклад використання списків
l = [1,2,3,4,5,6,7,8,9,0]
print("Список: ",l)
i = int(input("Введіть і (число яке пропускає попередні і власне значення): "))
if not l.count(i)==0:    # або if l.count(i)!=0:
    while i < 9:
        print(l[i], end=" ")
        i += 1
else:
 print("Дане число не входть в список")

"---------------item--(l[:2])------------------------"
#Видалення по ідексах, зрізи
l=[1,4,7]
print(l[:2])      # видаляє третій елемент (у Python нумерація починається з нуля, а не з одиниці)
"---------------Кортеж-(менша вага, ніж у списках)- без наступних змін даних-----------------------"
A=(1,2,3,4,5,6,7,8,9)   # Кортеж не можливо потім змінити
B=[1,2,3,4,5,6,7,8,9]
C=tuple(input("Введіть речення, яке плануєте розбити на знаки/літери: "))    # tuple() - розбиття на складові
print('Кортеж - ',A.__sizeof__(),' bytes') # розмір у байтах
print('Список - ',B.__sizeof__(),' bytes')
print(C)
"----------------------tuple---------------------------"
running = True
while running:
    l= tuple(input("Заповніть список: "))
    n=input("Виберіть шуканий знак: ")
    print("Знайдено знаків",n,": ",l.count(n))

    if n == '!' or l.count('!')>=1:
        running = False
else:
    print('End of the cycle...')
"-----------------------Словник-{}--------------------------"
#'S1' - ключ із значенням :
D1={'S1':4,'S2':5}
print('S1: ',D1['S1'])
print('S2: ',D1['S2'])
#або dict:
D2=dict(S3='Mike',S4='Shevchenko')
D2['S3']=input("Введіть нове імя: ")
D2['S4']=input("Введіть нове прізвище: ")
print(D2)
#або [] кортеж:
D3=dict([('key_1',input('key_1: ')),('key_2',input('key_1: '))])
print(D3)
#або fromkeys - створення значень ключів  - для усіх значень a і b присвоюється:
D5=dict.fromkeys(['a','b','c','d','e','g'],input('Введіть нове жначення для усіх нових клчів: '))
print(D5)
#або- через цикл:
D6={A:A**2 for A in range(11)} #range -у проміжку, запис квадратів чисел проміжку до 10
print('Квадрати чисел: ',D6,end="")


# Приклад запису бази даних студента:
student ={'name':{'last name':'Шевченко', 'first name':'Михайло','middle name':'Сергійович'},'adress':['м.Львів',
'вул.Пачічна','буд.62-Б','к.407'],'tell':{'t_first':'380683168590','t_second':"3-99-11", 't_third':"Іди в ж#пу"}}
print(student['name']['first name']) #пошук по ключам
print(student['adress'][1])
print("Values: ",student.values())
print("Keys: ",student.keys())

# Власний приклад:
d = {'name':'Mike', 'surname':'Shevchenko'}
print(d, ' None')

d1 = dict (name = 'Mike', surname = 'Shevchenko')
print(d1, ' dict(x='',y='')')

d2 = dict.fromkeys(['name','surname'])
d2['name'] = 'Mike'
d2['surname'] = 'Shevchenko'
print(d2, ' dict.fromkeys([x,y])')

d3 = {a: a**2 for a in range (1,8)}
print(d3, ' for a in range')

#d3.clear() # Очищує списки

d4 = d2  # посилання повне
d2['n'] = 'New'
print(d2)
print(d4)

d5 = d2.copy()
d2.pop('n')
print(d2,'без n ')
print(d5,'з n, бо копія ' )

d2['name']='Ivan'
d2['surname']='Golubosh'
print(d2)
d5.update(d2)
print(d5)

"--------------------Ще один приклад---------------------------------------------"
#Шидевр-р-р
l = tuple(input("Заповніть список: "))
i = (input("Введіть ключовий знак: "))
if l.count(i) != 0:
     print("Даний знак присутній у списку", l.count(i), "раз(-ів)")
else:
    print("Елемент ", i, " відсутній у списку")

"--------------------Нейронка-------Sigmoid--------------------------------------"
from numpy import exp, array, random, dot
training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = array([[0, 1, 1, 0]]).T                              # ще ясно
random.seed(1)                                                              # аve рандом
synaptic_weights = 2 * random.random((3, 1)) - 1                            # задаємо ваги за формулою
for iteration in range(1000):                                               # задаємо кількість ітерацій (1000) у циклі
    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))   # дофіга сигмоїда
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))# зміна ваг
    до певного моменту, поки  training_set_inputs-->training_set_outputs ('вчимо' нейронку)
print (1 / (1 + exp(-(dot(array([1, 0, 0]), synaptic_weights)))))              # "пока, кожаные... "
"---------------------Множина-------Set-------frozenset-------------in-------------len---------update------------"
# Робота з множинами 'SET'
A=set("hello")                                          # задаємо множину
f=['q','w','e','r','t','u','u','q']
B={'b1',11}
print(A," ",B)
C = {i**2 for i in range(10)} #запис через цикл for
print(type(C)) #Рандомний порядок виводу множини
print(C)
"--------------------------------"
D=frozenset('Mike') #'Кортежний' (одноразовий) ввід множини
A.add(12)
B.add(13)
print(A,' ',D)
"--------------------------------"
print(set(f))  # Вивід списку f як множини (без повторень одинакових знаків)
"--------------------------------"
print (len(f)) # Вивід довини списку f
"--------------------------------"
x1 = 'q'
print(x1 in f)  # Показує, чи є 'x' у 'f'
"--------------------------------"
x2 = {1,12,23,44,55,66,77,88,92,}; f2={9,8,7,6,5,4,3,2,1}
print(f2.isdisjoint(x2)) # Показує,чи немає  x2 у f2
f2.update(x2); print(f2) # Доповрює множину f2 множиною х2
"--------------------------------"
x2.remove(66); print(x2) # Видаляє вказаний елемент
"--------------------------------"
x2.add(66); print(x2) # Додає вказаний елемент
"--------------------------------"
x2.discard(66); print(x2) # Видаляє вказаний елемент, якщо він присутній у множині
(на відміну від remove не видає помилок при відсутності вказаного елемента )
"--------------------------------"
x2.pop(); print(x2)   # Видаляє рандомний (перший) елемент
"--------------------------------"
x2.clear(); print(x2) # Очищує множину
"----------------Фунції---def-add-return--------lambda-------------------------------------"
def f(x,y,z):
    res = ((x ** 2) + (y ** 2) + (z ** 2))
    return res
print(f(2,2,2))
"--------------------------------"
# Калькулятор трохи
def func(x):
    def add(y):        # додає(У)
        return x + y   # ф-ла (1)
    return add
t1 = int(input("X: "))
test = func(t1)
t2 = int(input("Y: "))
print("X+Y=",test(t2))   # підставляє введені значення х та у у формулу (1)
"--------------------------------"
def f(x):
    pass # функція нічого не повертає
print(f())
"--------------------------------"
def f(x,y,a=5):  # (x+y)^a
    res  = x+y
    res **= a
    return res
print("(x+y)^a=",f(int(input("X: ")),int(input("Y: "),)))
"--------------------------------"
def f2 (*args): # *коли не вказано кількіть змінних - КОРТЕЖ
    return args
print(f2(1,2,3))
"--------------------------------"
def f3 (**args2): # **словник
    return  args2
print(f3(short='dict',longer="dictionary"))
"--------------------------------" 
def f4 (**args3):
    return args3
print(f4(short='dict',longer="dictionary"))
add = lambda x,y: x*y
"--------------------------------"
print(add(2,5))  # запис через lambda - без return
print((lambda x,y:x*y)(2,6)) # ще один запис через lambda (коротший)
"--------------------------------"
fun = lambda *args:args # ще один запис через lambda
print(fun(1,2,3))
"----------------Виключення (print(10/0) or print(A/0)) -----try---except-----------------------------"
# Програма, яка ділить цілі числа і виключає випадок ділення на 0, а також виключає ділення букв
running = True
while running:
    try:
        x = int(input("Введіть х:"))
        y = int(input("Введіть y:"))
    except ValueError:
        print("Ви ввели не число!")
        x=0; y=0
    else:                                                   #Якщо все ок (було введено число)
        print("Все вірно",end=" ")
    finally:                                                #В будь-якому випадку
         print("100%")
    try:
        res = x/y
    except ZeroDivisionError:
        print("На нуль ділити не можна!")
        res=0
    print("Відповідь: ",res)
    print('')
    if x == 0 or y == 0:
        running = False
else:
    print('End of the cycle...')
"-----------------------------Робота з файлами -------------------------------------------------------------"
# Читаєм з файла:
f = open('text.txt','r')
print(f.read())
for line in f:
    print(line)
# Записуєм у файл:
f = open('text.txt','w')
f.write('Hi, it\'s me, Mario!') # \' - запис риски апострофа
f.write('\n123') # \n - запис з нового рядка
"-----------------Менеджери --With...as---encoding----------------------------------------------------------"
# Збереження критичних функцій Open,close при роботі з файлами
# Закриття фалів при спробі записати букву замість цифри
with open ('test1.txt','wt',encoding='utf-8') as inFile:
    num = int (input(":"))
    line = str('1/'+str(num)+"="+str(1/num))
    print(line)
    inFile.write(line)
"---------------------------Модулі--import--from------------------------------------------------------------------------"
# Імпорт бібліотек
import math
import time
import os
import random as r
import module
print("Число Pi: ", math.pi)
print(time.time())
print(os.getcwd())
print(os.getlogin())
print(r.random())
"---------------------------"
import module
module.hi()                #Підклчення бібліотеки, ствреної вручну
print(module.add(1,2))
"-----------from----------------"
from module import  hi as h,add as a  # Конкретна вибірка по нeобхідних підмодулях модуля module
h()
print(a(15,56))
"---------------------------ООП------------------------------------------------------------------------"
# Створення обєктів на основі класів
class Person:
    name = ""
    age = 

ivan = Person()
ivan.name = "Ivan"
ivan.age = 21
print(ivan.name,",",ivan.age)

vlad = Person()
vlad.name ="Vlad"
vlad.age = 35
print(vlad.name,",",vlad.age)
"---------------------------"
# Функції (методи) у ООП:
class Person():
    name = "Mike"
    age = 21

    def set (self, name, age):
        self.name = name
        self.age = age

vlad = Person ()
vlad.set ("Влад", 25)
print (vlad.name + " " + str(vlad.age))

'--------------------------------------'
class Person():
    type = 'custom_type'
    name = 'custom_name'
    age = 'custom_age'

p1 = Person ()
p1.name = 'Mike'
p1.age = 22
p1.type = 'student'
print('This is ',p1.type,'',p1.name,', and he/she has ',p1.age,'.')
"-------------------Наследование, инкапсуляция, полиморфизм--------------------------"
# 'Наслідування' - створений клас наслідує усі поля, функції, методи із основного класу
# _ не варто використовуавти цей метод в інших класах
# __ строга заборона
# поліморфізм -- додавання строк print (vlad.name + " " + str(vlad.age))
class Person():
    name = "Mike"
    names = "Sh"
    age = 21

    def set (self, name, names, age):
        self.name = name
        self.names = names
        self.age = age

class Student(Person):
    course = 5

mike = Student()
mike.set("Mike","Shevchenko",21)
print(mike.name,mike.names,", курс:",mike.course)
"--------------------Конструкторы, переопределение методов--------------------------------"
# Конструктор - ф-ція __init__:
class Person():
    name = "Mike"
    names = "Sh"
    age = 21

    def __init__(self, name, names, age):
        self.name = name
        self.names = names
        self.age = age

class Student (Person):
    course = 1

    def set(self, name, names, age, course):      # добавляєм course у __set
        self.name = name
        self.names = names
        self.age = age
        self.course = course

mike = Student ("Mike","Sh",21)
#mike.set ("Mike",21)     # Пропускає цей складний рядок
mike.set ("Міша","Шевченко",21,5)
print ("Імя -",mike.name,", прізвище -", mike.names,", вік -",mike.age,", курс -", mike.course)
"---------------------------------------Декоратори--------------------------------------------------------"
# 'обгортки' для фунції - виконання коду після і до самої ф-ції
# сповільнюють код
def decorator (func):
    def wrapper():
        print ("Код до виконання ф-ції")
        func()
        print ("Код який виконався після ф-ції")
    return  wrapper
@decorator           # фіча для більш красивішої декорації
#@decorator          # якщо мало одного)
def show ():
    print("Я звичайна ф-ція")
#show = decorator (show)    # декоруєм    # при @decorator цей рядок не є необхідним
show ()
"----------------------Кінець відеоуроків---Гоша Дударь-------------------------------------------------"  """
