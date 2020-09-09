print('Просте присвоювання...')
shoplist = ['хліб','мазік','помідори','цибуля','банани','печиво "Вушка"','апельсин']

mylist = shoplist

del shoplist[0]
print('shoplist - ', shoplist)
print('mylist   - ', mylist)

print('\nКопіювання за допомогою простої вирізки... ')

mylist = shoplist [:]
del mylist[0]
print('shoplist - ', shoplist)
print('mylist   - ', mylist)