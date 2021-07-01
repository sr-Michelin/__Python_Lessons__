# Послідовність

shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
st_name = tuple('Shevchenko')

# Індексація
for i in range(len(shoplist)):
    print('Елемент ', i, ' - ', shoplist[i])

print('\n{0}'.format(st_name))

# Вирізка із списку
print('\nЕлементи з 1 по 3 - ', shoplist[0:3])
print('Усі елементи - ', shoplist[:])

# Перевертання списку
print('\nПеревертання списку')
print(shoplist[::-1])

# Перевертання строки
print('\nПеревертання строки')
print(st_name[::-1])

# Вирізка із строки
print('\nЕлементи з 1 по 3 строки- ', st_name[0:3])
print('Усі елементи строки - ', st_name[:])

