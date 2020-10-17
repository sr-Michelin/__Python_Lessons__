"-----------------------Словник-{}--------------------------"
#'S1' - ключ із значенням :
'''D1={'S1':4,'S2':5}
print('S1: ',D1['S1'])
print('S2: ',D1['S2'])
#або dict:
D2=dict(S3='Mike',S4='Shevchenko')
D2['S3']=input("Введіть нове імя: ")
D2['S4']=input("Введіть нове прізвище: ")
print(D2)
#або [] кортеж - невменяєма х#ета:
D3=dict([('key_1',input('key_1: ')),('key_2',input('key_1: '))])
print(D3)
#або fromkeys - створення значень ключів  - для усіх значень a і b присвоюється:
D5=dict.fromkeys(['a','b','c','d','e','g'],input('Введіть нове жначення для усіх нових клчів: '))
print(D5)
#або- через цикл:
D6={A:A**2 for A in range(11)} #range -у проміжку, запис квадратів чисел проміжку до 10
print('Квадрати чисел: ',D6,end="")'''


# Приклад запису бази даних студента:
'''student ={'name':{'last name':'Шевченко', 'first name':'Михайло','middle name':'Сергійович'},'adress':['м.Львів','вул.Пачічна','буд.62-Б','к.407'],'tell':{'t_first':'380683168590','t_second':"3-99-11", 't_third':"Іди в ж#пу"}
print(student['name']['first name']) #пошук по ключам
print(student['adress'][1])
print("Values: ",student.values())
print("Keys: ",student.keys())'''

# Власний приклад:
'''d = {'name':'Mike', 'surname':'Shevchenko'}
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
d5.update(d2) # Обновлятор
print(d5)'''

"--------------------Ще один приклад---------------------------------------------"
#Шидевр-р-р
'''l = tuple(input("Заповніть список: "))
i = (input("Введіть ключовий знак: "))
if l.count(i) != 0:
     print("Даний знак присутній у списку", l.count(i), "раз(-ів)")
else:
    print("Елемент ", i, " відсутній у списку")'''

