# Способи перевантаження операторів у класах
class Clock:
    __DAY = 86400  # к-сть секунд у дні

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError('Секунди мають бути цвлочисельними')

        self.__secs = secs % self.__DAY

    def get_format_time(self):
        s = self.__secs % 60
        m = (self.__secs // 60) % 60
        h = (self.__secs // 3600) % 24
        print(f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}')

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else '0' + str(x)

    def get_seconds(self):
        return self.__secs

    @staticmethod
    def __oth(method):
        if not isinstance(method, Clock):
            raise ArithmeticError('Усі оператори мають бути типу "Clock"!')

    def __add__(self, other):
        """Для операції коректної типу с1 + с2 використовують перезагрузку операторів "__add__":"""
        Clock.__oth(other)
        return Clock(self.__secs + other.get_seconds())

    def __sub__(self, other):
        """Для операції коректної типу с1 - с2 використовують перезагрузку операторів "__sub__":"""
        Clock.__oth(other)
        return Clock(self.__secs + other.get_seconds())

    def __mul__(self, other):
        """Для операції коректної типу с1 * с2 використовують перезагрузку операторів "__mul__":"""
        Clock.__oth(other)
        return Clock(self.__secs * other.get_seconds())

    def __truediv__(self, other):
        """Для операції коректної типу с1 / с2 використовують перезагрузку операторів "__truediv__":"""
        Clock.__oth(other)
        return Clock(self.__secs / other.get_seconds())

    def __floordiv__(self, other):
        """Для операції коректної типу с1 // с2 використовують перезагрузку операторів "__floordiv__":"""
        Clock.__oth(other)
        return Clock(self.__secs // other.get_seconds())

    def __mod__(self, other):
        """Для операції коректної типу с1 % с2 використовують перезагрузку операторів "__mod__":"""
        Clock.__oth(other)
        return Clock(self.__secs % other.get_seconds())

    def __iadd__(self, other):
        """Для операції коректної типу с1 += с2 використовують перезагрузку операторів "__iadd__":"""
        Clock.__oth(other)
        self.__secs += other.get_seconds()
        return self

    def __isub__(self, other):
        """Для операції коректної типу с1 -= с2 використовують перезагрузку операторів "__isub__":"""
        Clock.__oth(other)
        self.__secs -= other.get_seconds()
        return self

    def __imul__(self, other):
        """Для операції коректної типу с1 -= с2 використовують перезагрузку операторів "__imul__":"""
        Clock.__oth(other)
        self.__secs *= other.get_seconds()
        return self

    def __itruediv__(self, other):
        """Для операції коректної типу с1 /= с2 використовують перезагрузку операторів "__truediv__":"""
        Clock.__oth(other)
        self.__secs /= other.get_seconds()
        return self

    def __ifloordiv__(self, other):
        """Для операції коректної типу с1 //= с2 використовують перезагрузку операторів "__ifloordiv__":"""
        Clock.__oth(other)
        self.__secs //= other.get_seconds()
        return self

    def __imod__(self, other):
        """Для операції коректної типу с1 %= с2 використовують перезагрузку операторів "__imod__":"""
        Clock.__oth(other)
        self.__secs %= other.get_seconds()
        return self

    def __eq__(self, other):
        """Для операції коректної типу с1 == с2 використовують перезагрузку операторів "__eq__":"""
        Clock.__oth(other)
        return self.__secs == other.get_seconds()

    def __nq__(self, other):
        """Для операції коректної типу с1 != с2 використовують перезагрузку операторів "__eq__" із "not":"""
        Clock.__oth(other)
        return not self.__eq__(other)
        # return self.__secs != other.get_seconds() # або так

    """Для операторів типу '>', '<', '<=', '>=' є опис за посиланням 
    'https://proproprogs.ru/python_oop/peregruzka-operatorov' """

    def __getitem__(self, item):
        """Для доступу до об'\єкта за ключем"""
        if not isinstance(item, str):
            raise ValueError('Ключ може бути тільки текстовим!')

        if item == 'hour':
            return (self.__secs // 3600) % 24
        if item == 'min':
            return (self.__secs // 60) % 60
        if item == 'sec':
            return self.__secs % 60

        return 'Неправильний ключ'

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Ключ може бути тільки текстовим!')
        elif not isinstance(value, int):
            raise ValueError('Значення може бути тільки цілочисельним!')

        s = self.__secs % 60
        m = (self.__secs // 60) % 60
        h = (self.__secs // 3600) % 24

        if key == 'hour':
            self.__secs = s + 60 * m + value * 3600
        if key == 'min':
            self.__secs = s + 60 * value + h * 3600
        if key == 'sec':
            self.__secs = value + 60 * m + h * 3600


c1 = Clock(10000)
c2 = c1
c3 = Clock(10000)
c4 = Clock(10000)

# "c1 + c2" == "c1__add__(self, c2)":
(c1 + c2 + c3 + c4).get_format_time()

# "c1 += c2" == "c1.__iadd__(self, c2)":
c1 += c2
c1.get_format_time()

# а можна і так:
c1 += c2 + c3 + c4
c1.get_format_time()

# ітд...

# Для перевірки типу c1 == x2 застосовується "__eq__(self, other)":
print(c1 == c2)

# Для перевірки типу c1 != x2 застосовується "__eq__(self, other) із not":
print(c1 != c2)

# Для доступу до об'\єкта за ключем
print(f"{c1['hour']}:{c1['min']}:{c1['sec']}")

# Для присвоєнні певному ключу певного значення (c1['key'] = value):
c1['hour'] = 24
print(f"{c1['hour']}:{c1['min']}:{c1['sec']}")