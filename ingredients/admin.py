from django.contrib import admin
from .models import Ingredient

# Add model to admin view
admin.site.register(Ingredient)