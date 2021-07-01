from django.shortcuts import render
from .models import News, Category


# Create your views here - контроллери

def index(request):
    """Вивід новин і початкового тексту"""
    news = News.objects.all()
    # news = News.objects.order_by('-created_at')  # для відображення найновіших новин зверху
    categories = Category.objects.all()

    context = {
        'news': news,
        'title': 'Список новин',
        'categories': categories,
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'categories': categories, 'category': category})
