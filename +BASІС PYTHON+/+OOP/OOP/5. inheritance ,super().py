# Спосіб, поданий нижче, є неефективним (дублювання коду, порушення прицмпів програмуванн), але показати його треба
print(
    'Спосіб, поданий нижче, є неефективним (дублювання коду, порушення принципів програмуванн), '
    'але показати його треба')
print('#-----' * 15 + '#')


class Point:
    def __init__(self, x=0, y=0):
        self.__x, self.__y = x, y

    def __str__(self):
        """Перерозподіл координат"""
        return f'({self.__x}, {self.__y})'


print(f'{issubclass(Point, object) = } -- клас "object" може бути підкласом "Point"')


class Line:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        """sp: Point, ep: Point, color: str = 'red', width: int = 1 -- підказка програмісту"""
        self.sp, self.ep, self.color, self.width = sp, ep, color, width

    def drawline(self):
        print(f'Малюю лінію: {self.sp}, {self.ep}, {self.color}, {self.width}')


class Rect:
    def __init__(self, sp: Point, ep: Point, color: str = 'black', width: int = 10):
        """sp: Point, ep: Point, color: str = 'black', width: int = 10 -- підказка програмісту"""
        self.sp, self.ep, self.color, self.width = sp, ep, color, width

    def draw_rect(self):
        print(f'Малюю прямокутник: {self.sp}, {self.ep}, {self.color}, {self.width}')


li = Line(Point(1, 2), Point(10, 20))
li.drawline()

r = Rect(Point(30, 40), Point(70, 60))
r.draw_rect()

print('#-----' * 15 + '#')

# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#
# Наступний метод більш раціональний - наслідування:
# Спочатку запускається конструктор підкласу, потім батьківський
# Private - змінна батьківського класу може застосовуватися і у дочірних (при методі "get_width()")
print('# Наступний метод більш раціональний - наслідування:\n')


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        """sp: Point, ep: Point, color: str = 'red', width: int = 1 -- підказка програмісту;
        __width - приватна змінна, між підкласами не використовуєтья
        """
        self._sp, self._ep, self._color, self.__width = sp, ep, color, width
        print('Конструктор базового класу Prop')

    def get_width(self):
        """Для роботи із приватною змінною __width"""
        return self.__width


class Line(Prop):
    def __init__(self, *args):
        print('Перевизначений конструкор Line')
        # Prop.__init__(self, *args)
        super().__init__(*args)  # правилний порядок, гарно працює під час множинного наслідування
        self.__width = 5  # вішання локальних префіксів на приватні змінні (усі астрибути - через словник)

    def drawline(self):
        """Метод get_width() із батьківського класу дає доступ до приватної змінної __width"""
        print(f'Малюю лінію: {self._sp}, {self._ep}, {self._color}, {self.get_width()}, {self.__width} '
              f'(локальна ширина)')


class Rect(Prop):
    def __init__(self, *args):
        print('Перевизначений конструкор Rect')
        # Prop.__init__(self, *args)
        super().__init__(*args)  # правилний порядок, гарно працює під час множинного наслідування
        self.__color = 'black'  # вішання локальних префіксів на приватні змінні (усі астрибути - через словник)

    def draw_rect(self):
        """Метод get_width() із батьківського класу дає доступ до приватної змінної __width"""
        print(
            f'Малюю прямокутник: {self._sp}, {self._ep}, {self._color}, {self.get_width()}, {self.__color} '
            f'(локальний колір)')


li = Line(Point(1, 2), Point(10, 20))
li.drawline()
print(li.__dict__, '\n')

r = Rect(Point(30, 40), Point(70, 60))
r.draw_rect()
print(r.__dict__, '')

print('#-----' * 15 + '#')
input()
