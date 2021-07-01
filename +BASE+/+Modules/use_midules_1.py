from mymodule import L, K
import mymodule

L[0] = 10  # водночас замінюю два об\'єкти
print('Для змінного об\'єкту - списку:', L, mymodule.L, sep='\n')

K += (10,)  # зміни зачіпають тільки кортеж K (from mymodule import K створює новий об\'єкт)
print('Для незмінного об\'єкту - кортежу:', K, mymodule.K, sep='\n')

print('Вивід усіх зміних для mymodule:', dir(mymodule), sep='\n')


