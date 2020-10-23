print('Просте присвоювання...\
\nнаступний обєкт посилається на попередний')
shoplist = ['хліб', 'мазік', 'помідори', 'цибуля', 'банани', 'печиво "Вушка"', 'апельсин']

mylist = shoplist

del shoplist[0]
print('shoplist - ', shoplist)
print('mylist   - ', mylist)

print('\nКопіювання за допомогою простої вирізки... \
\nнаступний обєкт не посилається на попередний')

mylist = shoplist[:]
del shoplist[0]
print('shoplist - ', shoplist)
print('mylist   - ', mylist)
