n = 'Mike'
sn = 'Shevchenko'

print("І'мя %s, призвіще %s" % (n, sn))
print("І'мя {0}, призвіще {1}\n".format(n, sn))

t = 'text'
print('\a{0} -- '.format(t), '\\+a')  # дзвінок
print('\b{0} -- '.format(t), '\\+b')  # забій
print('\n{0} -- '.format(t), '\\+n')  # переніс
print('\f{0} -- '.format(t), '\\+f')  # переніс сторінки
print('\t{0} -- '.format(t), '\\+t')  # горизонтальна табуляція
print('\v{0} -- '.format(t), '\\+v')  # вертикальна табуляція
print('\0 -- '.format(t), '\\+0')  # Null

print(r'C:\newt.txt')  # відклчення екранування

m = ' mike '.title()
print(m.rstrip().lstrip())  # видалення відступів

print(f'My name is {m}')  # поєднання строки і змінної через f'str {}'

print(sn[::-1])  # перевертання строки -- зріз

print(
    sn.count('o', 0, 10))  # знаходження входженнь набору символів у стрічку із певними параметрами пошуку (тут [0,10))
