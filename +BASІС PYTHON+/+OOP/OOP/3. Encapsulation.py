# Основи роботи із закритими зміними класу

#   <атрибут> - public (публічний атрибут, можна змінювати зовні)
#  _<атрибут> - protected (можна використовувти всередині самого класу, а також у дочірних класах)
# __<атрибут> - private (тільки у самому класі)

class Point:
    WIDTH = 5

    # __slots__ = ['__x', '__y']  # дозволені атрибути екземплярів класу Point
    # для її правильної роботи забираємо перезагруженні методи типу "__<метод>__" (наприклад, "__getattr__")

    def __init__(self, x=0, y=0):
        """Ініціація координат"""
        self.__x, self.__y = x, y
        print('Створений екземпляр класу Point!'.upper())

    def __check_value(self):
        """Перевірка введених значень атрибутів на відповідність форматам
        __check_value - приватний метод класу"""
        if isinstance(self, int) or isinstance(self, float):
            return True
        else:
            return False

    def set_cords(self, x, y):
        """Задає нові кординати всередині класу -- СЕТТЕР"""
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x, self.__y = x, y
        else:
            print('\nВведені кординати не є чисельними!')

    def get_cords(self):
        """Виводить координати через внутрішню ф-цію "get_cords -- ГЕТТЕР"""
        print(f'Координати x,y: {self.__x, self.__y}')

    def __getattribute__(self, item):
        """Автоматично викликається при отриманні властивості класу із іменем item:
        val x == "Приватна змінна"
        """
        if item == '_Point__x':
            return '"Приватна змінна"'
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        """Збереження атрибутів класу від зовнішньої зміни"""
        if key == "WIDTH":
            print('\n"А тобі моя водичка для чого потрібна?!" - '
                  'Чорний Сталкер, коли хтось пробує змінити захищену внутрішню змінну "WIDTH" класу "Point"')
        else:
            self.__dict__[key] = value
            # self.__x = value # для появи RecursionError, так не робимо

    def __getattr__(self, item):
        """При введені неіснуючого атрибута у екземпляр класу виводить його і\'мя у консоль """
        print(f'\n__getattr__: {item}')

    def __delattr__(self, item):
        """При видаленні певного атрибута сповіщає у консоль його і\'мя"""
        print(f'\n__delattr__: {item}')


pt = Point()
# print(pt.__x)  # видає AttributeError, так як атрибут приватний
pt.get_cords()

# після зміни
pt.set_cords(11, 1)
pt.get_cords()

# якщо дуже хочемо здобути приватний атрибут:
print(f'{pt._Point__x} , {pt._Point__check_value()} -- із приватного методу (нелегально трохи :@ )')

# збереження атрибуту WIDTH від випадкової зміни поза класом
pt.WIDTH = 6

# при зверненні до неіснуючого атрибуту:
pt.new_atr

# при створенні певної властивості (value) атрибуту і подальшого її видалення:
pt.new_atr = 1
del pt.new_atr
