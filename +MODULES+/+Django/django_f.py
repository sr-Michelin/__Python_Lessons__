import os

cwd = os.getcwd()
print(cwd)

'''D:\DOCK\Python_M\venv\+LESSONS\+MODULES+\+Django'''

'''django-admin'''

'''cd f_site'''

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
# <h1>Mike</h1> --> Mike
# {% autoescape off %} {{body}} {% endautoescape %}  # вимкнення автоекранування певних символів - безпеки ради

# {% cycle 'text-danger' 'text-success' %} # cycle - тут ми змінюємо кольори заголовків

# {% filter %} {{body}} {% endfilter %} # фільтр
# {% firstof var1,var2,var3 %} # виводть перший елемент із True

# {% for item in items %} {{body}} {% endfor %} # ітератор
# or {% for key,value in data.items %} {{key}}:{{value}} {% endfor %} # ітератор у випадку словника
# {% forloop.counter %} {{body}} # ітератор, який видає номер ітерації
# {% for item in news %} {% empty %} <li>Елементи відсутні</li> {% endfor %} # при відсутності елементів -> текст про це

# {% if _condition %} or {% elif _condition %} or {% else %} # оператори if з and, or, not; ==,!=, <, >, >=, <=

# {% lorem [count] [method] [random] %}  (C - к-сть параграфів, M (w - слова, p - HTML, b -текстові параграфи),
# # random - виключає стандатрний шаблон lorem) # вивід випадкового тексту

# It is {% now 'js F Y h:i'%} # часовий тег

# {% spaceless %} <p> text </p> {% endspaceless%} # зжимає HTML-розмітку


'''photo'''
'''
<div class="container mt-3">
    <h1>{{title}}</h1>
    <div class="row">
      <div class="col-md-12">
      {% for item in news %}
      <div class="card mb-3">
        <div class="card-header">
          Категорія: {{ item.category }}
        </div>
        <div class="card-body">
          <div class= "media">
            {% if item.photo %}
              <img src="{{item.photo.url}}" alt="" width="350" align="left" hspace="10" class="mr-3">
            {% else %}
              <img src="https://static.dw.com/image/19312223_303.jpg" alt="" width="350" align="left" hspace="10"
                   class="mr-3">
            {% endif %}
            <div class="media-body">
                <h5 class="card-title">{{ item.title }}</h5>
                <p class="card-text">{{ item.content }}</p>
                <a href="#" class="btn btn-primary">Читай далі...</a>
            </div>
          </div>
      </div>
        
      <div class="card-footer text-muted">
        опубліковано: {{ item.created_at|date:"Y-m-d H:i:s" }}
      </div>
    </div>
    {% endfor %}
    </div>
  </div>
</div>
'''

'''Фільтри'''
# {{value|add:"2"}} # сума
# {{news.count}} # кількість елементів
# {{value|addslashes}} # добавляє "/"
# {{ value|capfirst }} # mike --> Mike
# {{ value|center:"1" }} # "Mike" ---> " Mike "
# {{ value|cut:" " }} # відрізає " "

# {{ value|date:"D d M Y" }} # 'Wed 09 Jan 2008'
# {{ value|date:"SHORT_DATE_FORMAT" }} "09/01/2008"

# {{ value|default:"Nope" }} # якщо value пуста, то виводить Nope
# {{ value|default_if_none:"Nope" }} # якщо value == None, то виводить Nope

# {{ value|dictsort:"name" }} # сортування значень словників

# {{ value|divisibleby:"3" }} # True, якщо value ділится на аргумент 3 цілочисельно

# {% autoescape off %} {{<h1>Mike</h1> } {% endautoescape %} # відключає аавтоекранування

# {{ value|filesizeformat }} # виводить розмір value у байтах

# {{ value|first }} # виводить перший елемент списку value
# {{ value|last }} # виводить останій елемент списку value

# {{ value|floatformat:"0" }} # округлення до певного знаку
# {{ value|floatformat:"3" }}
# {{ value|floatformat:"-3" }} # 34.00000 ----> 34

# {{ value|get_digit:"2" }} # 123456789 ---> 8

# {{ value|join:" // " }} # ['a', 'b', 'c'] --> "a // b // c"

# {{ value|length }} # ['a', 'b', 'c', 'd'] --> 4
# {{ value|length_is:"4" }} # True для ['a', 'b', 'c', 'd']

# {{ value|linebreaks }} # "Joel\nis a slug" --> "<p>Joel<br>is a slug</p"
# {{ value|linebreaksbr }} # "Joel\nis a slug" --> "Joel<br>is a slug"

# {{ value|linenumbers }} # one --> 1. one

# {{ value|lower }} # "ABCD" --> "abcd"
# {{ value|make_list }} "ABCD" --> ["A","B","C","D"]

# {{ value|phone2numeric }} # "800-COLLECT" --> "800-2655328" - з кнопкового телефона

# You have {{ num_messages }} message{{ num_messages|pluralize }} # if num_messages = 2 --> 2 messages

# {{ value|random }} # random from value

# {{ var|safe|escape }} # escape
# {{ some_list|safeseq|join:", " }} # safe для кожного із е-лтів

# {{ value|slugify }} # "Joel is a slug" --> "joel-is-a-slug"

# {{ blog_date|timesince:comment_date }} # стільки часу пройшло із певної дати
# {{ conference_date|timeuntil:from_date }} # час до певної дати

# {{ value|title }} # перший символ через CAPS

# {{ value|truncatechars:7 }} # "Joel is a slug" --> "Joel i…" - вкорочує по символах
# {{ value|truncatechars_html:7 }} # "Joel is a slug" --> "<p>Joel i…</p>"
# {{ value|truncatewords:2 }} # те саме що truncatechars, але вже по словах
# {{ value|truncatewords_html:2 }} # те саме що truncatechars_html, але вже по словах

'''Сайд-бар по категоріям'''
# views.py:
# categories = Category.objects.all()
#
#     context = {
#         'news': news,
#         'title': 'Список новин',
#         'category': categories,
#     }

# index.html:
#         <div class="container mt-3">
#     <h1>{{title}}</h1>
#     <div class="row">
#
#         <div class="col-md-2">
#             <div class="list-group">
#                 {% for item in categories %}
#                 <a href="/category/ {{item.pk}}" class="list-group-item list-group-item-action">{{item.title}}</a>
#                 {% endfor %}
#             </div>
#         </div>

# views.py
# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news': news, 'categories': categories, 'category': category})

# urls.py:
# urlpatterns = [
#     path('', index),
#     path('category/<int:category_id>', get_category),  # категорії на сайд-барі
# ]

# category.html

