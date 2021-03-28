from django.db import models

# Create your models here.

# Моделі опрацьовують дані за допомогою баз даних
# Атрибути SQL:
'''
id - INT
title - Varchar
content - Text
created_at - DateTime
updated_at - DateTime
photo - Image
is_published - Boolean
'''


class News(models.Model):
    """Атрибути новин:"""
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)  # може бути пустим
    created_at = models.DateTimeField(auto_now_add=True)  # зберігає дату при створені новини (один раз - без змін)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')  # збереження фото у директоріях по часу
    is_published = models.BooleanField(default=True)

    def __str__(self):
        """<QuerySet [<News: Новина №1>, <News: Новина №2>, <News: Новина №3>, <News: Новина №4>]>"""
        return self.title
