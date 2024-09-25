from django.contrib import admin
from .models import Ingredient

# Add model to admin view
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories')