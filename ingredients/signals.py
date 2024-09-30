# ingredients/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Ingredient

@receiver(post_save, sender=Ingredient)
def log_ingredient_save(sender, instance, created, **kwargs):
    if created:
        # Add to a logging system
        print(f"Ingredient '{instance.name}' added with {instance.calories} calories.")