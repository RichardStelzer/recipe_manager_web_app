from django.shortcuts import get_object_or_404, render

from .models import Recipe


def detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)

    print("------> Title: " + recipe.title)
    # print("------> Functions: ", dir(recipe))
    print("------> 'recipe.ingredientquantity_set.all()' ---> ", recipe.ingredientquantity_set.all())
    print("------> 'recipe.ingredientquantity_set.all()[0]' ---> ", recipe.ingredientquantity_set.all()[0])
    print("------> 'recipe.ingredientquantity_set.all()[0].quantity' ---> ", recipe.ingredientquantity_set.all()[0].quantity)
    print("------> 'recipe.ingredientquantity_set.all()[0].unit' ---> ", recipe.ingredientquantity_set.all()[0].unit)
    print(recipe.ingredients.all())

    # print(recipe.ingredients.all())
    # print(recipe.ingredients.all()[1].name)

    return render(request, "recipe/detail.html", {"recipe": recipe})
