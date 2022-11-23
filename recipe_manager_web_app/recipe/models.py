from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    brief_description = models.TextField()
    full_description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through="IngredientQuantity")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class Unit(models.Model):
    name = models.CharField(max_length=255, default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class IngredientQuantity(models.Model):  # Join the db tables
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    quantity = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe.title + " - " + self.ingredient.name

