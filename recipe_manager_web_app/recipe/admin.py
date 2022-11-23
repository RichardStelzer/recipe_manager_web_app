from django.contrib import admin

from .models import Unit, Ingredient, Recipe, IngredientQuantity

admin.site.register(Unit)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(IngredientQuantity)
