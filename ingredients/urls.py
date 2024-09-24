# ingredients/urls.py
from django.urls import path
from .views import add_ingredient, create_dish, ingredient_list

urlpatterns = [
    path('add/', add_ingredient, name='add_ingredient'),
    path('create_dish/', create_dish, name='create_dish'),
    path('list/', ingredient_list, name='ingredient_list'),
]