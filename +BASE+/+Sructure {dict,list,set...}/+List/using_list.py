# Програма, яка демонструє роботу із списками та циклами
# 'Нагадуваання'

import time as ti

shoplist = ['хліб', 'мазік', 'помідори', 'цибуля', 'банани', 'печиво "Вушка"', 'апельсин']
print('\nЯ мушу зробити', len(shoplist), 'покупок')

ti.sleep(1)
print('Мої покупки: ', end='')
for item in shoplist:
    print(item, end=',')

ti.sleep(1)
print("")
print('\nТакож хочу купити сіжки (не для себе):')
shoplist.append('сiжки "Danhel"')
print('Тепер список виглядає наступним чином: ', end='')
for item in shoplist:
    print(item, end=',')

ti.sleep(1)
print("")
print('\nВідсортую список:')
shoplist.sort()
print('Тепер список виглядає наступним чином: ', end='')
for item in shoplist:
    print(item, end=',')

ti.sleep(1)
print('\n\nЯ пішов в магазин...')
ti.sleep(1)

while not len(shoplist) == 0:
    print('\nЯ купив "%s"...' % (shoplist[0]))
    olditem = shoplist[0]
    print('Залишилося купити %s - всього лиш %s покупок' % (shoplist, len(shoplist)))
    del shoplist[0]
    ti.sleep(1)
else:
    print('\nЯ купив все!')
    input()
