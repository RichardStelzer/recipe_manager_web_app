from django.contrib import admin

from .models import Category, Unit, Ingredient, Rating, Recipe, IngredientQuantity

admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Ingredient)
admin.site.register(Rating)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # fields --> Entries on "recipe/<pk>/change/"
    # fields = ("title",)
    # list_display --> Selection on "recipe/"
    list_display = ("title", "author", "get_categories")

    def get_categories(self, instance):
        return [category.name for category in instance.categories.all()]


# admin.site.register(Recipe)
admin.site.register(IngredientQuantity)
