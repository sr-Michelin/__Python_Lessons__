# Послідовність

shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
name = tuple('Shevchenko')

# Індексація
for i in range (len(shoplist)):
    print('Елемент ',i,' - ', shoplist[i])
print('\n{0}'.format(name))

# Вирізка із списку
print('\nЕлементи з 1 по 3 - ', shoplist[0:3])
print('Усі елементи - ', shoplist[:])

# Вирізка із строки
print('\nЕлементи з 1 по 3 строки- ', name[0:3])
print('Усі елементи строки - ', name[:])

