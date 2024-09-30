# ingredients/views.py
from django.shortcuts import render, redirect

from .forms import IngredientForm, DishForm
from .models import Ingredient
from django.core.cache import cache


def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()
    
    return render(request, 'ingredients/add_ingredient.html', {'form': form})

def create_dish(request):

    ingredients = cache.get('ingredient_list')
    if not ingredients:
        ingredients = Ingredient.objects.all()
        cache.set('ingredient_list', ingredients, timeout=300)  # Cache for 5 minutes
    

    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            selected_ingredients = form.cleaned_data['ingredients']
            total_calories = sum(ingredient.calories for ingredient in selected_ingredients)

            return render(request, 'ingredients/dish_result.html', {
                'ingredients': selected_ingredients,
                'total_calories': total_calories
            })
    else:
        form = DishForm()


    return render(request, 'ingredients/create_dish.html', {'form': form})

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredients/ingredient_list.html', {'ingredients': ingredients})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # Redirect to a category list page or other appropriate page
    else:
        form = CategoryForm()

    return render(request, 'ingredients/add_category.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'ingredients/category_list.html', {'categories': categories})