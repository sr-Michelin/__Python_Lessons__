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

'''////////////////CRUD////////////////'''
# from news.models import News

'''запис нового запису'''
# News(title='Новина №1', content='Контент новини №1')
# news = News  # news = _
# news.id
# news.save() # збереження обєкта публікації
# news.id

'''SQL запит у вигляді словника'''
# from django.db import connection
# connection.queries # SQL запит у вигляді словника
# news.pk # news.id - первинний ключ запису, який доступний після збереження запису

'''запис нового запису'''
# news2 = News(title='Новина №2', content='Контент новини №2') - запис другої новини
# news2.save()

'''ще один запис нового запису'''
# news3 = News()
# news3.title = 'Новина №3'
# news3.content = 'Контент новини №3'
# news3.save()

'''без збереження через save()'''
# news4 = News.objects.create(title='Новина №4', content='Контент новини №4')  # вже без збереження через save()


'''перегляду усіх новин'''
# News.objects.all() - для перегляду усіх новин
# news = _  # ітератор
# for item in news:
#    print(item.title, item.is_published)

'''фільтр'''
# News.objects.filter(title = 'Новина №1')
# News.objects.get(pk = 1) - для одного значення - по pk

'''присвоєння нових значеннь старим записам:'''
# News.objects.get(pk = 4)
# news3 = _
# news3.pk = 3
# news3.save()

'''видалення запису:'''
# news9 = News.objects.get(pk = 9)
# news9.delete()

'''виведення за певним порядком - сортування'''
# News.objects.order_by('title')
# News.objects.order_by(-'title') # зворотній порядок

'''викючення певного запису у виводі (не у базі:)'''
# News.objects.exclude(title = 'Новина №4')
'''////////////////CRUD////////////////'''

'''Рендер ШАБЛОНІВ із контролерів (The template layer)'''
# templates/news/index.html
# views.py  --  render(request, template_name='news/index.html', context=context)

'''Superuser (Одмен)'''
# python manage.py createsuperuser (admin, admin@localhost, admin)
# models.py ---- class Meta

# admin.py  ---- admin.site.register(News, NewsAdmin)  # реєструєм блок News для адміна
# admin.py  ---- list_display, list_display_links, search_fields

'''Зовнішний вигляд'''
# https://getbootstrap.com/docs/5.0/components

'''Теги'''
# {% for item in news %}
