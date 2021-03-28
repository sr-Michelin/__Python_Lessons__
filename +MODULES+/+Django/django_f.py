import os

cwd = os.getcwd()
print(cwd)

'''django-admin'''

'''cd \f_site'''

# тестовий запуск:
'''first_dj_site>python manage.py runserver'''
'''first_dj_site>python manage.py runserver 4000'''
'''first_dj_site>python manage.py runserver 1.2.3.4:4000'''

# добавлення веб-застосунку(аплікації) news - папки із пакетами:
'''first_dj_site>python manage.py startapp news'''

# controller - news.views  --- між даними і їх відображеннями

# у Django моделі описуються класами

# migration - модуль змін (створення полів на основі моделей)
# python manage.py makemigrations   --> створення міграції із модуля (0001_initial.py)
# python manage.py sqlmigrate news 0001
# python manage.py migrate   ---> застосунок міграцій

# формування маршруту для медіа файлів у режимі відладки

# python manage.py shell -- інтерактивна консоль Django:

'''////////////////////////////////'''
# from news.models import News

# News(title='Новина №1', content='Контент новини №1')
# news = News  # news = _
# news.id
# news.save() # збереження обєкта публікації
# news.id

# from django.db import connection
# connection.queries # SQL запит у вигляді словника
# news.pk # news.id - первинний ключ запису, який доступний після збереження запису

# news2 = News(title='Новина №2', content='Контент новини №2') - запис другої новини
# news2.save()

# news3 = News()
# news3.title = 'Новина №3'
# news3.content = 'Контент новини №3'
# news3.save()

# news4 = News.objects.create(title='Новина №4', content='Контент новини №4')  # вже без збереження через save()


# News.objects.all() - для перегляду усіх новин

# news = _  # ітератор
# for item in news:
#    print(item.title, item.is_published)

# News.objects.filter(title = 'Новина №1') # фільтр
