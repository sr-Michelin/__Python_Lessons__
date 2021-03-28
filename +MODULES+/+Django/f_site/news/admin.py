from django.contrib import admin
from .models import News, Category


# адмінка на новинах

class NewsAdmin(admin.ModelAdmin):
    """Означення відображення властивостей новин для адмінки"""
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')  # клікабельні посилання
    search_fields = ('title', 'content')  # можливість пошуку

    list_editable = ('is_published',)  # checkbox
    list_filter = ('is_published', 'category')  # фільтр


class CategoryAdmin(admin.ModelAdmin):
    """Означення відображення властивостей категорії новин для адмінки"""
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')  # клікабельні посилання
    search_fields = ('title',)  # можливість пошуку


admin.site.register(News, NewsAdmin)  # реєструєм блок News для адміна
admin.site.register(Category, CategoryAdmin)  # реєструєм блок Category для адміна
