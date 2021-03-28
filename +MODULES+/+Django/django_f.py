import os

cwd = os.getcwd()
print(cwd)

'''django-admin'''

'''cd D:\DOCK\Python_M\vеnv\+LESSONS\+MODULES+\+Django\f_site'''

# тестовий запуск:
'''first_dj_site>python manage.py runserver'''
'''first_dj_site>python manage.py runserver 4000'''
'''first_dj_site>python manage.py runserver 1.2.3.4:4000'''

# добавлення веб-застосунку(аплікації) news - папки із пакетами:
'''first_dj_site>python manage.py startapp news'''

# controller - news.views  --- між даними і їх відображеннями
