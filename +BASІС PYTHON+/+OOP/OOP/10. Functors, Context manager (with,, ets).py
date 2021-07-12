# Функтори і менеджери контексту
# Функтори - об'\єкти класу, які можуть використовуватися як ф-ції

class Counter:
    """Клас - лічильник"""

    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        self.__counter += 1
        print(f'{self.__counter = }', end=' ')
        return self.__counter


# виклик функтора (із кожним подальшим викликом зростає "self.__counter")
c1 = Counter()
c1(), c1(), c1()
print()

# незалежність екземплярів лічильників
c2 = Counter()
c2(), c2(), c2()
print()

# ---------------Strip()---------------------------------
print('#' + '--' * 10)


class StripChars:
    """Функтор, який забирає у початку і у кінці стрічки певні символи (з набору)"""

    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError('Аргумент має бути стрічкоий!')

        return args[0].strip(self.__chars)


s1 = StripChars('!@#$%^&*()"')
print(s1('"Hello World!"'))


# Цей функтор є еквівалентим функції замикання, яка на практиці використовується частіше:
def strip_chars_f(chars):
    def string_strip(string):
        if not isinstance(string, str):
            raise ValueError('Аргумент має бути стрічкоий!')
        return string.strip(chars)

    return string_strip


s2 = strip_chars_f('!@#$%^&*()"')
print(s2('"Hello World!"'))

# ---------------Менеджери контексту---------------------------------
# Менеджери контексту - класи (автоматичне закриття файлового потоку після виконання пених дій)
# із методами "__enter__()", "__exit__()"
print('#' + '--' * 10)


# приклад такого менеджера
# with open('10_text.txt') as fp:
#    """тут ''__enter__'' повертає посилання на файловий потік, а ''__exit__'' закриває його у кінці роботи"""
#    for line in fp:
#        print(line)

# власний приклад
class DefenderVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        """Копіємо в-р v"""
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:  # якщо не було ніяких виключень:
            self.__v[:] = self.__temp  # запис у v1 "__temp"
        return False  # "False" для передачі помилки вище, при "True" програма не реагує на "IndexError"


# два в-ри одинакової довжини - корекне додавання
v1 = [1, 2, 3]
v2 = [1, 2, 3]

try:
    with DefenderVector(v1) as dv:
        for i in range(len(dv)):
            dv[i] += v2[i]

except IndexError as e:
    print(e)

print(v1)  # при "IndexError" цей список не змінюється на відмінну від звичайної роботи менеджера

# приклад вкладеного менеджера
try:
    with open('in.txt') as f_in:
        with open('out.txt') as f_out:
            for line in f_in:
                f_out.write(line)
except Exception as e:
    print(e)
