# ingredients/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

# ingredients models
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    calories = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        validators=[MinValueValidator(0.1)]  # Ensure calories can't be zero or negative
    )

    def __str__(self):
        return self.name

    def clean(self):
        if self.calories <= 0:
            raise ValidationError('Calories must be a positive number.')