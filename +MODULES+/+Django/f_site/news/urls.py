from django.urls import path
from .views import *

# збереження списку маршрутів зберігаємо у апці, а не в скелеті самого сайту (так забезпечується незалежність апок)
# відкидання лишніх адрес (/news/test)
urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>', get_category, name='category'),  # категорії на сайд-барі
]
