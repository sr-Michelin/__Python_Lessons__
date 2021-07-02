class Point:
    x = 1
    y = 1


pt = Point()
pt.x, pt.y = 10, 11

print(f"{getattr(pt, 'x')}, {getattr(pt, 'y')} -- атрибути x та y")  # getattr -- видає вміст атрибута

print(
    f'{getattr(pt, "z", False)} -- виклик відсутього атрибута "z" видає "False"')  # більш гнучкий спосіб (без помилок)

print(f'{hasattr(pt, "y")}, бо атрбут "y" існтує у системі')  # hasattr -- перевірка присутності атрибута

print(f"{setattr(pt, 'z', 11)} -- новий атрибут 'z'")  # setattr -- задає атрбут
print(f'{pt.__dict__} - вивід словника атрибутів')

pt.z = 100
pt.msg = "hello"  # ще один спосіб задавання атрибута
delattr(pt, 'msg')  # видалення атрибута
print(f'{pt.__dict__} - вивід словника атрибутів')
print(isinstance(pt, Point), ', бо pt екземпляр класу Point')  # перевірка належності
