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
    # зберігає дату при створені новини (один раз - без змін):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    # збереження фото у директоріях по часу, може бути пустим:
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано?')
    # зв\'язок News і Category через ForeignKey:
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категорія')

    def __str__(self):
        """Новина №1,... замість news_№1,..."""
        return self.title

    class Meta:
        verbose_name = 'Новина'  # об/'єкт однина
        verbose_name_plural = 'Новини'  # об/'єкт множина
        ordering = ['created_at']  # сортування об/'єктів


class Category(models.Model):
    """Поділ на категорії"""
    # поле є швидшим для пошуку:
    title = models.CharField(max_length=150, db_index=True, verbose_name='Назва категорії', blank=True)

    def __str__(self):
        """по аналогії (Культура, Спорт, Політика, Наука,... замість Section_1,...)"""
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
