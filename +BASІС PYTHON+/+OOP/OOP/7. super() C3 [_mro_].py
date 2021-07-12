# Множинне наслідування
# Згадуєтья алгоритм C3 MRO -- обхід дерева наслідування із батьківським класом "object"

# Ієрархія класів
# У випадку Line(Pos, Styles) --> Line(Styles, Pos) отримуємо рекурсію, а, одже, і помлку
print('# -----------Error---------------- ')


class Point:
    def __init__(self, x=0, y=0):
        self.__x, self.__y = x, y

    def __str__(self):
        return f'({self.__x}, {self.__y})'


class Styles:
    def __init__(self, colour='black', width=10):
        print('Констуктор "Styles"')
        self._colour, self._width = colour, width


class Pos:
    def __init__(self, sp: Point, ep: Point, *args):
        print('Констуктор "Pos"')
        self._sp, self._ep = sp, ep
        # передача параметрів *args (для правильного виклику екземпляру Lisne)
        Styles.__init__(self, *args)


class Line(Pos, Styles):
    """Нмножинне наслідування із двох класів"""

    def draw(self):
        print(f'Малюю лінію із параметрами: {self._sp},  {self._ep},  {self._colour},  {self._width}')


li = Line(Point(10, 10), Point(11, 11), 'green')
li.draw()

# -----------------------------------------
print('# ------------super()------------- ')


# Обходить усіх батьківських класів у одному порядку один раз - без рекурсії
# *args - для перестановок; викликається кожний раз для різних класів
# (властивості не путаються між наслідуваними класами)

class Styles:
    def __init__(self, colour='black', width=10, *args):
        print('Констуктор "Styles"')
        self._colour, self._width = colour, width
        super().__init__(*args)


class Pos:
    def __init__(self, sp: Point, ep: Point, *args):
        print('Констуктор "Pos"')
        self._sp, self._ep = sp, ep
        # передача параметрів *args (для правильного виклику екземпляру Lisne)
        super().__init__(*args)


class Line(Pos, Styles):
    """Нмножинне наслідування із двох класів"""

    def draw(self):
        print(f'Малюю лінію із параметрами: {self._sp},  {self._ep},  {self._colour},  {self._width}')


li_1 = Line(Point(11, 0), Point(0, 11), 'yellow', 12)
li_1.draw()

# ------------ Line(Pos, Styles)-----------
print('# -----super() без *args----------- ')


class Styles:
    def __init__(self):
        print('Констуктор "Styles"')
        super().__init__()


class Pos:
    def __init__(self):
        print('Констуктор "Pos"')
        super().__init__()


class Line(Pos, Styles):
    """Нмножинне наслідування із двох класів"""

    def __init__(self, sp: Point, ep: Point, colour='red', width=0):
        self._sp = sp
        self._ep = ep
        self._colour = colour
        self._width = width
        super().__init__()

    def draw(self):
        print(f'Малюю лінію із параметрами: {self._sp},  {self._ep},  {self._colour},  {self._width}')


li_2 = Line(Point(), Point(), 'orange', 35)
li_2.draw()
print(f'{Line.__mro__ = } -C3')  # обхід дерева наслідування

input()
