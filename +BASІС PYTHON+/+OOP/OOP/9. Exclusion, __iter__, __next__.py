# Створення виключень та ітерабельних класів
# "__iter__" - викликається, коли об'\єкт береться для ітерації типу it = MyIter(18)
# "__next__" - викликається, коли у циклі "for" відбувається перехід до наступого значення

import random

import colorama
from colorama import init
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


class CoordError(Exception):
    """Власний клас опрацювання виключень"""
    pass


class ImageXIteration:
    def __init__(self, img, y: int):
        self.__limit = img.width
        self.__y = y
        self.__img = img
        self.__x = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__x >= self.__limit:
            raise StopIteration

        self.__x += 1
        return self.__img[self.__x - 1, self.__y]


class ImageYIteration:
    def __init__(self, img):
        self.__limit = img.height
        self.__img = img
        self.__y = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__y >= self.__limit:
            raise StopIteration

        self.__y += 1
        return ImageXIteration(self.__img, self.__y - 1)


class Image:
    """Клас для зберігання кліп-арт зображень"""

    def __init__(self, width, height, background='+'):
        self.__background = background
        self.__pixels = {}
        self.__width = width
        self.__height = height
        self.__colors = {self.__background}

    @property
    def width(self):
        """Повертає ширнину"""
        return self.__width

    @width.setter
    def width(self, width):
        """Записує ширнину"""
        self.__width = width

    @property
    def height(self):
        """Повертає висоту"""
        return self.__height

    @height.setter
    def height(self, height):
        """Записує висоту"""
        self.__height = height

    def __check_coord(self, coord):
        if not isinstance(coord, tuple) or len(coord) != 2:
            raise CoordError('Координати мають подаватися тільки у вигляді двохвимірного кортежу')

        if not (0 <= coord[0] < self.__width) or not (0 <= coord[1] < self.__height):
            raise CoordError('Значення координати виходть за межі зображення')

    def __setitem__(self, coord, color):
        """Задавання параметрів кольору та координат"""
        self.__check_coord(coord)

        if color == self.__background:
            """Якщо колір пікселя рівний кольору екрану, то видаляємо цей піксель"""
            self.__pixels.pop(coord, None)
        else:
            """у іншому випадку добавлямо у словник ключ "coord" і його значення "color", 
            а також добавлямо колір у палітру"""
            self.__pixels[coord] = color
            self.__colors.add(color)

    def __getitem__(self, coord):
        self.__check_coord(coord)
        return self.__pixels.get(coord, self.__background)

    def __iter__(self):
        return ImageYIteration(self)


'''class MyIter:
    """Ітерабельний клас"""

    def __init__(self, limit):
        self.__num = 0
        self.__limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.__num >= self.__limit:
            raise StopIteration

        self.__num += 1
        return self.__num'''

img = Image(20, 4)

# задаємо кортежу координат кольори
img[random.randint(0, img.width - 1), random.randint(0, img.height - 1)] = f'{Fore.RED}@'
img[random.randint(0, img.width - 1), random.randint(0, img.height - 1)] = f'{Fore.YELLOW}*'
img[random.randint(0, img.width - 1), random.randint(0, img.height - 1)] = f'{Fore.LIGHTYELLOW_EX}+'
img[random.randint(0, img.width - 1), random.randint(0, img.height - 1)] = f'{Fore.GREEN}%'
img[random.randint(0, img.width - 1), random.randint(0, img.height - 1)] = f'{Fore.CYAN}₴'

colour = img[1, 1]  # зчитування певного кольору певного пікселя (за координатами)

# print(f'{img.height, img.width = }')
# print(f'{colour = }')

# вивід загального екрану із певним пікслем (без методів - ітераторів)
print('Вивід загального екрану із певним пікслем (без методів - ітераторів):')
for y in range(img.height):
    for x in range(img.width):
        print(img[x, y], sep=' ', end=' ')
    print()

# Чисельна демонстрація роботи класу MyIter із метод
"""it = MyIter(11)
print('Iterable MyIter():', end=' ')
for i in it:
    print(i, sep=',', end=' ')"""


# вивід загального екрану із певним пікслем (із методом - ітератором)
print('\nВивід загального екрану із певним пікслем (із методом - ітератором):')
for row in img:
    for pixel in row:
        print(pixel, sep=' ', end=' ')
    print()
