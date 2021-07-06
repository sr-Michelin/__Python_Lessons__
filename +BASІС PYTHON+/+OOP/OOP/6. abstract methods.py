# Перевизначення публічних методів, робота як із статичними

class Point:
    def __init__(self, x=0, y=0):
        self.__x, self.__y = x, y

    def __str__(self):
        return f'({self.__x}, {self.__y})'

    def is_digit(self):
        """Перевірка на правильність введення координат"""
        if (isinstance(self.__x, int) or isinstance(self.__x, float)) and (
                isinstance(self.__y, int) or isinstance(self.__y, float)):
            return True
        else:
            return False

    def is_int(self):
        """Перевірка на цілочисельність координат"""
        if (isinstance(self.__x, int)) and (isinstance(self.__y, int)):
            return True
        else:
            return False


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp, self._ep, self._color, self._width = sp, ep, color, width

    def set_cords(self, sp, ep):
        if sp.is_digit() or ep.is_digit():
            # зміна локальних параметрів при умові правильності введення координат
            self._sp, self._ep = sp, ep
        else:
            print('Кординати задані хибно!')


class Line(Prop):
    def draw_line(self):
        print(f'Малюю лінію: {self._sp}, {self._ep}, {self._color}, {self._width}')

    def set_cords(self, sp: Point, ep: Point):
        """Перевірка на цілочисельність"""
        if sp.is_int() and ep.is_int():
            # self._sp, self._ep = sp, ep
            Prop.set_cords(self, sp, ep)  # більш гнучкіший метод
        else:
            print('Серед ведених координат є дані типу "float"!')


l = Line(Point(10, 1), Point(26, 11))
l.draw_line()

# Перезапис координат через set_cords при умові is_digit
l.set_cords(Point(1, 1), Point(2, 2))
l.draw_line()

print('-' * 40)


# -----------------------------------------
# Перезагрузка операторів

class Point:
    def __init__(self, x=0, y=0):
        self.__x, self.__y = x, y

    def __str__(self):
        return f'({self.__x}, {self.__y})'

    def is_digit(self):
        """Перевірка на правильність введення координат"""
        if (isinstance(self.__x, int) or isinstance(self.__x, float)) and (
                isinstance(self.__y, int) or isinstance(self.__y, float)):
            return True
        else:
            return False

    def is_int(self):
        """Перевірка на цілочисельність координат"""
        if (isinstance(self.__x, int)) and (isinstance(self.__y, int)):
            return True
        else:
            return False


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp, self._ep, self._color, self._width = sp, ep, color, width

    def set_cords(self, sp, ep):
        if sp.is_digit() or ep.is_digit():
            # зміна локальних параметрів при умові правильності введення координат
            self._sp, self._ep = sp, ep
        else:
            print('Кординати задані хибно!')

    def draw(self):
        """У випадку відсутності методу draw() викликається помилка.
        Абстактний метод у цьому випадку потребує перевизначення у дочірніх класах (імітація абстакції)
        """
        raise NotImplementedError('У дочірному класі має бути визначеним метод draw()')


class Line(Prop):
    def draw(self):
        print(f'Малюю лінію: {self._sp}, {self._ep}, {self._color}, {self._width}')

    def set_one_coord(self, sp):
        if sp.is_int():
            self._sp = sp
        else:
            print('Координата має бути цілочисельною')

    def set_two_coord(self, sp, ep):
        if sp.is_int() and ep.is_int():
            Prop.set_cords(self, sp, ep)
        else:
            print('Серед ведених координат є дані типу "float"!')

    def set_cords(self, sp: Point, ep: Point = None):
        """Перевірка на цілочисельність"""
        if ep is None:
            self.set_one_coord(sp)
        else:
            self.set_two_coord(sp, ep)


class Rect(Prop):
    def draw(self):
        print(f'Малюю прямокутник: {self._sp}, {self._ep}, {self._color}, {self._width}')


class Ellipse(Prop):
    def draw(self):
        print(f'Малюю еліпс: {self._sp}, {self._ep}, {self._color}, {self._width}')


l = Line(Point(-10, 1), Point(26, 11))
l.draw()

# Перезапис координат через set_cords при умові is_digit
l.set_cords(Point(1, 1), Point(2, 2))
l.draw()

# Робота із одною координатою через перевантаження
l.set_cords(Point(-19, -3))
l.draw()
print('-' * 40)

# -----------------------------------------
# Подача багатьох фігур через списки

fig = []

fig.append(Line(Point(0, 0), Point(1, 1)))
fig.append(Rect(Point(1, 1), Point(0, 0)))
fig.append(Ellipse(Point(1, 1), Point(0, 0)))

for item in fig:
    item.draw()
print('...ітд')
print('-' * 40)

# -----------------------------------------
