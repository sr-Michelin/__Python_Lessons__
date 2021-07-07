# Публічна змінна є доступною і одинаковою для усіх створених екземплярів #
import random

print('#-----' * 15 + '#')


class Point:
    count = 0


def idp(P):
    """Виконує рутинну роботу (перевірка ID трьох об\'єктів, вивід кінцевого списку)"""

    t = id(P[0].count) == id(P[1].count) and id(P[0].count) == id(P[2].count)
    print('\nВідображення властивостей змінної "count":',
          'True, екземпляри посилаються на одну публічну змінну' if t
          else 'False, екземпляри не посилаються на одну публічну змінну')
    print(f'Список екземплярних змінних "count": {[p.count for p in P]}')


P = [Point(), Point(), Point()]

# Статична властивість публічної змінної "count" (усі екземпляри посилаються на одну публічну змінну)
Point.count = 1
idp(P)

# Створення одної локальної змінної з індексом "1"
P[random.randint(0, 2)].count = 1
Point.count = 0
idp(P)
print('#-----' * 15 + '#')


# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#
# Створення локальної змінної через __init__(автоматично при створенні екземпляра)

class Point:
    __count = 0

    def __init__(self, x=0, y=0):
        Point.__count += 1
        self.cordX, self.cordY = x, y

    @staticmethod  # встановлення статусу "статичного" методу нижче (self вже не є обов\'язковим у get_count())
    def get_count():
        print(f'Значення лічильника "count": {Point.__count = }')


P = [Point(), Point(), Point()]

P[0].__count = 1  # присвоєння порушує статичність
print(f'Список екземплярних змінних "count": {[p._Point__count for p in P]} -- посилання на один об\'єкт')
Point.get_count()
print('#-----' * 15 + '#')


# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#
# Створення "Синглетона" - класу із одним доступним екземпляром

class Point:
    __count = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        """Створення екземпляру Point перезавантаженням;
        cls посилається на Point"""
        if not isinstance(cls.__instance, cls):
            """Якщо параметр 'cls.__instance' не рівний 'cls', створюється екземпляр класу"""
            cls.__instance = super(Point, cls).__new__(cls)
        else:
            print('Езкемпляр даного класу вже існує...')

    def __init__(self, x=0, y=0):
        Point.__count += 1
        self.cordX, self.cordY = x, y

    @staticmethod  # встановлення статусу "статичного" методу нижче (self вже не є обов\'язковим у get_count())
    def get_count():
        print(f'Значення лічильника "count": {Point.__count = }')


P = [Point(), Point(), Point()]

# Таким чином ми створєм один екземпляр-оригінал і решту його копій із одинаковим ID
print([id(p) for p in P])
input()