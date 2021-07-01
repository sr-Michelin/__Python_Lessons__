import mymodule as mm

mm.say_hello()

print(f'{mm.PI = }')
mm.PI = 3.14  # зміна елемента модуля mymodule (без змін у самому модулі)
print(f'{mm.PI = } -- new data')

# перезавантаження модуля (стандартний модуль зазпускається тільки раз -- для оптимізації)
import importlib

importlib.reload(mm)
print(f'\n{mm.PI = } - перезавантаження через importlib')

print('\nВерсія ' + mm.__version__)
