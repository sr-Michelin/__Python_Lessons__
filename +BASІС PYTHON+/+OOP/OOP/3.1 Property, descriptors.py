# Об\'єкти - властивості

# Є два типи дескипторів:
# - data
# - non-data

class Point:
    def __init__(self, x=0, y=0):
        self.__x, self.__y = x, y
        print('Створений новий екземпляр!')

    def __check_value(self):
        if isinstance(self, int) or isinstance(self, float):
            return True
        else:
            return False

    def __get_cord_x(self):
        """Читання значень з атрибутів"""
        print(f'Виклик get_cord_x - зчитування з [{self.__x = }]')
        return self.__x

    def __set_cord_x(self, x):
        """Запис значень у атрибути"""
        print(f'Виклик set_cord_x - запис у [{self.__x = }]')
        if Point.__check_value(x):
            self.__x = x
        else:
            raise ValueError('Неправильний формат вводу')

    def __del_cord_x(self):
        print(f'видалення властивості [{self.__x = }]')
        del self.__x

    # створення властивості, яка буде використовувати ГЕТТЕР і СЕТТЕР для зчитування та запису
    coordX = property(__get_cord_x, __set_cord_x, __del_cord_x)


pt = Point()
pt.coordX = 2.5e4  # запис властивостей
x = pt.coordX  # зчитування властивостей
print(f'{x = }')
del pt.coordX  # видалення властивостей-

# ----------------------------------------------
print('\nДаний клас можна переписати через @декоратори [@property, @cord_x.setter, @cord_x.deleter]:')


class Point_0:
    def __init__(self, x=0, y=0):
        self.__x, self.__y = x, y
        print('Створений новий екземпляр!')

    def __check_value(self):
        if isinstance(self, int) or isinstance(self, float):
            return True
        else:
            return False

    @property
    def cord_x(self):
        """Читання значень з атрибутів"""
        print(f'Виклик get_cord_x - зчитування з [{self.__x = }]')
        return self.__x

    @cord_x.setter
    def cord_x(self, x):
        """Запис значень у атрибути"""
        print(f'Виклик set_cord_x - запис у [{self.__x = }]')
        if Point.__check_value(x):
            self.__x = x
        else:
            raise ValueError('Неправильний формат вводу')

    @cord_x.deleter
    def cord_x(self):
        print(f'видалення властивості [{self.__x = }]')
        del self.__x


pt = Point_0(1, 2)
pt.coordX = 2.5e4  # запис властивостей
x = pt.coordX  # зчитування властивостей
print(f'{x = }')
del pt.coordX  # видалення властивостей

pt.coordX = 1
print(f'{pt.coordX = }')

# ----------------------------------------------
print('\nДобавим ще cordY через дескриптори:')


class CoordValue:
    """Дескриптор - клас із трьома методами: [__get__, __set__, __delete__]"""

    def __init__(self, name):
        """Локальна властивість зберігається у приватній змінній 'name' """
        self.__name = name

    def __get__(self, instance, owner):
        """Зчитування;
        Через instance звертаємось до створеного екземпляру класу;
        Згодом, через "__dict__" записуємо або зчитуємо значення
        """
        # return self.__value
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        """Запис"""
        # self.__value = value
        instance.__dict__[self.__name] = value

    def __delete__(self, obj):
        """Видалення"""
        del self.__value


class Point:
    """Клас, який посилаючись на клас-дескриптор, створює нові екземпляри у вигляді координат"""
    coordX = CoordValue('coordX')
    coordY = CoordValue('coordY')

    def __init__(self, x=0, y=0):
        """Присвоєення конструктором локальних координат;
        Викликання методу при створенні нового екземпляру
        """
        self.coordX, self.coordY = x, y


pt = Point(1, 1)
pt.coordX, pt.coordY = 2, 2
print(f'{pt.coordX, pt.coordY = }')

pt1 = Point(1, 1)
pt1.coordX, pt1.coordY = 3, 3
print(f'{pt1.coordX, pt1.coordY = }')

# pt, pt1 тепер не посилаються на один же об'\єкт, а записуються у вигляді ел-тів словника

# ----------------------------------------------
print('\nАналогічний запис через метод "__set_name__" -- для Python >= 3.6:')


# Є два типи дескипторів:
# - data
# - non-data


class CoordValue_:
    """Дескрипотр - клас із трьома методами: [__get__, __set__, __delete__]
    DATA - дескриптор"""

    def __set_name__(self, owner, name):
        """ Викликається автоматично при створенні дескриптора і зберігає у "name" значення coordX, coordY"""
        # print(name)
        self.__name = name

    def __get__(self, instance, owner):
        """Зчитування;
        Через instance звертаємось до створеного екземпляру класу;
        Згодом, через "__dict__" записуємо або зчитуємо значення
        """
        # return self.__value
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        """Запис"""
        # self.__value = value
        instance.__dict__[self.__name] = value

    def __delete__(self, obj):
        """Видалення"""
        del self.__value


class NonDataDescr:
    """Тільки для зчитування;
    NON_DATA - дескриптор"""

    def __get__(self, instance, owner):
        return "NonDataDescr __get__"


class Point:
    """Клас, який посилаючись на клас-дескриптор, створює нові екземпляри у вигляді координат"""
    non_data = NonDataDescr()

    coordX = CoordValue_()
    coordY = CoordValue_()

    def __init__(self, x=0, y=0):
        """Присвоєення конструктором локальних координат;
        Викликання методу при створенні нового екземпляру
        """
        self.coordX, self.coordY = x, y


pt = Point(1, 1)
pt.coordX, pt.coordY = 2, 2
print(f'{pt.coordX, pt.coordY = }')

pt1 = Point(1, 1)
pt1.coordX, pt1.coordY = 3, 3
print(f'{pt1.coordX, pt1.coordY = }')

pt1.non_data = 'hello'.upper()
print(f'\n{pt1.non_data = } -- робота, як із стрічкою, а не із декриптором')
input()
