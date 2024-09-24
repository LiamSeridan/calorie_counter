# calorie_counter/urls.py (main URL configuration)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingredients/', include('ingredients.urls')),
]