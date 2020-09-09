
shoplist = ['хліб','мазік','помідори','цибуля','банани','печиво "Вушка"','апельсин',]
print('Я мушу зробити',len(shoplist),'покупок')

print('Мої покупки: ',end='')
for item in shoplist:
    print(item,end=',')

print("")
print('\nТакож хочу купити сіжки (не для себе):')
shoplist.append('сiжки "Danhel"')
print('Тепер список виглядає наступним чином: ',end='')
for item in shoplist:
    print(item,end=',')

print("")
print('\nВідсортую список:')
shoplist.sort()
print('Тепер список виглядає наступним чином: ',end='')
for item in shoplist:
    print(item,end=',')

'''print("")
print('\nПерше, що я маю купити: ',shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купив: ',olditem)
print('Тепер список виглядає наступним чином: ',end='')
for item in shoplist:
    print(item,end=',')'''


