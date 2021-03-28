from django.urls import path
from .views import index

# збереження списку маршрутів зберігаємо у апці, а не в скелеті самого сайту (так забезпечується незалежність апок)
# відкидання лишніх адрес (/news/test)
urlpatterns = [
    path('', index),
    # path('test/', test),
]
