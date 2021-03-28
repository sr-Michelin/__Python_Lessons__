from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    print(request)
    return HttpResponse('<h1>It is my first site!</h1>')


def test(request):
    return HttpResponse('<h1>Testing page...</h1>')
