age = 22
name = 'Mike'

print('Я {0}, і мені {1} роки'.format(name, age))
print('{0} любить Python. {0} хоче стати програмістом!'.format(name))

# заокруглення за допомогою format()
num = 3.141618
print('{0:.2f}'.format(num))

# назви полів
print('{name} - have {0} years '.format(22, name='Mike'))

# вибір із списку
L = ['a', 'b', 'c']
print('{0[1]}'.format(L))

# вибір із словника
D = {
    'fname': 'Mike',
    'lname': 'Sh'
}
print('{0[fname]} {0[lname]}'.format(D))

# специфікатори перетворення
import decimal

print('{0} {0!s} {0!r} {0!a}'.format(decimal.Decimal('3.14')))

# Специфікатори формату
s = 'The sword of truth'
print('{0:25}'.format(s))  # мінімальна довина поля виводу 25
print('{0:>25}'.format(s))  # вирівнювання зправа
print('{0:^25}'.format(s))  # вирівнювання по центру
print('{0:-^25}'.format(s))  # заповнювач по центру
print('{0:->25}'.format(s))  # заповнювач зліва
print('{0:.10}'.format(s))  # максимальна довжина поля виоду

maxwidth = 12
print('{0}'.format(s[:maxwidth]))  # витяг зрізу ==>
print('{0:.{1}}'.format(s, maxwidth))  # ==>  вкладене замісне поле

# добавлення нулів
print('{0:0=12}'.format(123456789))  # нуль - заповнювач
print('{0:012}'.format(123456789))  # нуль - дроповнення
print('{0:*<15}'.format(123456789))  # * - символ-заповнювач

# вивід знака через format()
print('[{0:+}], [{1:+}]'.format(10, -10))  # обов'язково
print('[{0:-}], [{1:-}]'.format(10, -10))  # за потребою

# використання символів типом управління
print('{0:b}, {0:o}, {0:x}, {0:X}'.format(11))
print('{0:#b}, {0:#o}, {0:#x}, {0:#X}'.format(11))

# вивід чисел в [експ] і [норм] формах
import math

amount = (10 ** 3) * math.pi
# мінімальна ширина поля виводу - 12, 2 знаки після десяткової точки
print('[{0:12.2e}], [{0:12.2f}]'.format(amount))  # сток
print('[{0:*>12.2e}], [{0:*>12.2f}]'.format(amount))  # + заповнювач "*"
print('[{0:*>+12.2e}], [{0:*>+12.2f}]'.format(amount))  # + заповнювач "*" + обов'язковий вивід знака

# Форматування комплексних чисел
print('{0.real:.3f} {0.imag:+3f}j'.format(1 + 2j))
print('{0.real:.0f} {0.imag:+1f}j'.format(1 - 2j))
