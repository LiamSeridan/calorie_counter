# ingredients/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Ingredient
from .forms import IngredientForm, DishForm

# Model Tests
class IngredientModelTest(TestCase):
    
    # create ingredient
    def test_create_ingredient(self):
        """Test that an Ingredient object can be created."""
        ingredient = Ingredient.objects.create(name='Tomato', calories=20)
        self.assertEqual(ingredient.name, 'Tomato')
        self.assertEqual(ingredient.calories, 20)
    
    # check string for ingredient
    def test_string_representation(self):
        """Test the string representation of an ingredient."""
        ingredient = Ingredient(name='Tomato', calories=20)
        self.assertEqual(str(ingredient), 'Tomato')

# Form Tests
class IngredientFormTest(TestCase):

    # test ingredient form
    def test_valid_ingredient_form(self):
        """Test that the IngredientForm is valid with correct data."""
        form = IngredientForm(data={'name': 'Tomato', 'calories': 20})
        self.assertTrue(form.is_valid())
    
    # invalid form
    def test_invalid_ingredient_form(self):
        """Test that the IngredientForm is invalid with missing data."""
        form = IngredientForm(data={'name': '', 'calories': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)  # both fields should raise errors

# testing dish form
class DishFormTest(TestCase):

    def setUp(self):
        self.ingredient1 = Ingredient.objects.create(name='Tomato', calories=20)
        self.ingredient2 = Ingredient.objects.create(name='Cheese', calories=100)

    def test_dish_form_valid(self):
        """Test that DishForm is valid when ingredients are selected."""
        form = DishForm(data={'ingredients': [self.ingredient1.id, self.ingredient2.id]})
        self.assertTrue(form.is_valid())

    def test_dish_form_no_ingredients(self):
        """Test that DishForm is invalid if no ingredients are selected."""
        form = DishForm(data={'ingredients': []})
        self.assertFalse(form.is_valid())

# View Tests
class IngredientViewTests(TestCase):

    def test_add_ingredient_view_get(self):
        """Test that the add_ingredient view renders properly on GET request."""
        response = self.client.get(reverse('add_ingredient'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ingredients/add_ingredient.html')

    def test_add_ingredient_view_post(self):
        """Test that a POST request adds a new ingredient."""
        response = self.client.post(reverse('add_ingredient'), {
            'name': 'Tomato',
            'calories': 20
        })
        self.assertEqual(response.status_code, 302)  # should redirect after successful POST
        self.assertTrue(Ingredient.objects.filter(name='Tomato').exists())

class CreateDishViewTests(TestCase):

    def setUp(self):
        self.ingredient1 = Ingredient.objects.create(name='Tomato', calories=20)
        self.ingredient2 = Ingredient.objects.create(name='Cheese', calories=100)

    def test_create_dish_view_get(self):
        """Test that the create_dish view renders correctly on GET."""
        response = self.client.get(reverse('create_dish'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ingredients/create_dish.html')

    def test_create_dish_view_post(self):
        """Test that the POST request calculates the total calories."""
        response = self.client.post(reverse('create_dish'), {
            'ingredients': [self.ingredient1.id, self.ingredient2.id]
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Total Calories: 120')

# Integration Test
class IngredientAndDishIntegrationTest(TestCase):

    def test_add_ingredient_and_create_dish(self):
        """Test the complete flow from adding ingredients to creating a dish."""
        
        # Add an ingredient
        response = self.client.post(reverse('add_ingredient'), {
            'name': 'Lettuce',
            'calories': 5
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Ingredient.objects.filter(name='Lettuce').exists())

        # Now use it in a dish
        ingredient = Ingredient.objects.get(name='Lettuce')
        response = self.client.post(reverse('create_dish'), {
            'ingredients': [ingredient.id]
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Total Calories: 5')