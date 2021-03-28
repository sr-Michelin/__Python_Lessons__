from django.shortcuts import render
from django.http import HttpResponse
from .models import News


# Create your views here - контроллери

def index(request):
    """Вивід новин і початкового тексту"""
    news = News.objects.all()
    # news = News.objects.order_by('-created_at')  # для відображення найновіших новин зверху
    context = {
        'news': news,
        'title': 'Список новин'
    }
    return render(request, template_name='news/index.html', context=context)
