from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


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
    ingredients = models.ManyToManyField(Ingredient, through="IngredientQuantity", related_name='ingredients')
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name="categories")
    base_portions = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def average_rating(self):
        print("--------------->", Rating.objects.filter(recipe=self))
        return Rating.objects.filter(recipe=self).aggregate(Avg("rating"))["rating__avg"] or "Not rated yet"

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class Unit(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class IngredientQuantity(models.Model):  # Join the db tables
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    quantity = models.FloatField(default=1)

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "IngredientQuantities"    # The plural name for the object (https://docs.djangoproject.com/en/4.1/ref/models/options/)

    def __str__(self):
        return self.recipe.title + " - " + self.ingredient.name


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    rating = models.IntegerField(default=0)

    def __str__(self):
        return str(self.rating)
