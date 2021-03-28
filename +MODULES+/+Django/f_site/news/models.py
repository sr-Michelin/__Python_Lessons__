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
    title = models.CharField(max_length=150, verbose_name='Назва')
    content = models.TextField(blank=True, verbose_name='Контент')  # може бути пустим
    # зберігає дату при створені новини (один раз - без змін)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    # збереження фото у директоріях по часу, може бути пустим
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано?')

    def __str__(self):
        """<QuerySet [<News: Новина №1>, <News: Новина №2>, <News: Новина №3>, <News: Новина №4>]>"""
        return self.title

    class Meta:
        verbose_name = 'Новина'  # об/'єкт однина
        verbose_name_plural = 'Новини'  # об/'єкт множина
        ordering = ['created_at']  # сортування об/'єктів
