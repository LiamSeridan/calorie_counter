# ingredients/urls.py
from django.urls import path
from .views import add_ingredient, create_dish, ingredient_list, add_category, category_list

# Url endpoints
urlpatterns = [
    path('add/', add_ingredient, name='add_ingredient'),
    path('create_dish/', create_dish, name='create_dish'),
    path('list/', ingredient_list, name='ingredient_list'),
    path('add_category/', add_category, name='add_category'),
    path('categories/', category_list, name='category_list'),
]