from django.shortcuts import render
from django.http import HttpResponse
from .models import News


# Create your views here.

def index(request):
    """Вивід новин і початкового тексту"""
    news = News.objects.all()
    '''res = '<h1>Список новин</h1>'
    for item in news:
        res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n<div>\n<hr>\n'

    # return HttpResponse(['<h1>It is my first site!</h1>', res])
    # print(request)
    # return HttpResponse(res)'''
    return render(request, 'news/index.html', {'news': news, 'title': 'Список новин'})


#def test(request):
#   return HttpResponse('<h1>Testing page...</h1>')'''
