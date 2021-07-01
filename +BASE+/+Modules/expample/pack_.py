import packrand.fucs

from packrand import *  # імпорт тільки із "__init__.py" //якщо не використовується м-д "__all__"//

print(dir(packrand))  # усі зміні пакету packrand

print(packrand.fucs.func(0), '-- модуль із пакету packrand')  # застосування модуля із пакету packrand

print(f'{use_f.A = } -- вивід через "*" внутрушньопакетного використання модулів - use_f')
