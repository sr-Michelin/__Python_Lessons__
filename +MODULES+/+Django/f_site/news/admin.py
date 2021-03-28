from django.contrib import admin
from .models import News


# адмінка на новинах

class NewsAdmin(admin.ModelAdmin):
    """Означення відображення властивостей новин для адмінки"""
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title', 'is_published')  # клікабельні посилання
    search_fields = ('title', 'content')  # можливість пошуку


admin.site.register(News, NewsAdmin)  # реєструєм блок News для адміна
