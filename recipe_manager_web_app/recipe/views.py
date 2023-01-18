from django.shortcuts import get_object_or_404, render

from .models import Category, Recipe, Rating

from django.db.models import Q


def detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)

    # Update ingredient portions
    new_ingredient_quantities = []
    if request.method == "GET":
        portions = request.GET.get("portions")
        print("Request.GET content of input field ----->", portions)
        if portions is not None:
            for ingredient in recipe.ingredientquantity_set.all():

                multiplier = int(portions) / recipe.base_portions
                ingredient.quantity *= multiplier
                new_ingredient_quantities.append((ingredient.ingredient.name,
                                                  ingredient.quantity,
                                                  ingredient.unit.name))

                print("unit: ", ingredient.unit.name)
                print("quantity: ", ingredient.quantity, ", ingredient: ", ingredient.ingredient.name)
                print("base_portions: ", recipe.base_portions, ", portions: ", portions)
                print("multiplier: ", multiplier)
        else:
            portions = recipe.base_portions

    print("new_ingredient_quantities: ", new_ingredient_quantities)
    print(type(recipe.ingredientquantity_set.all()[0].quantity))
    print(recipe.ingredientquantity_set.all()[0].quantity)

    print("------> Title: " + recipe.title)
    # print("------> Functions: ", dir(recipe))
    print("------> 'recipe.ingredientquantity_set.all()' ---> ", recipe.ingredientquantity_set.all())
    print("------> 'recipe.ingredientquantity_set.all()[0]' ---> ", recipe.ingredientquantity_set.all()[0])
    print("------> 'recipe.ingredientquantity_set.all()[0].quantity' ---> ", recipe.ingredientquantity_set.all()[0].quantity)
    print("------> 'recipe.ingredientquantity_set.all()[0].unit' ---> ", recipe.ingredientquantity_set.all()[0].unit)
    print("------> 'recipe.ingredients.all()' ---> ", recipe.ingredients.all())
    print("------> 'recipe.category_set.all()' ---> ", recipe.categories.all())
    print("AAAAAA ---> ", type(recipe.ingredientquantity_set.all()[4].unit.name))
    # print(recipe.ingredients.all())
    # print(recipe.ingredients.all()[1].name)
    # print(portions)

    return render(request, "recipe/detail.html", {"recipe": recipe,
                                                  "new_ingredient_quantities": new_ingredient_quantities,
                                                  "portions": portions})


def category(request, slug):

    if slug == "all":
        # display list with all categories
        print("Category.objects.all() ------>", Category.objects.all())
        message = "List of Categories"
        categories = Category.objects.all()

        context = {
            "show_all_categories": True,
            "message": message,
            "categories": categories,
        }
        print("----------------->", context)
        return render(request, "recipe/category.html", context)

    category = get_object_or_404(Category, slug=slug)
    message = "Recipes of the category \'" + category.name + "\'"

    # print("Category to be displayed ------>", category)
    # print("Recipe objects ---------------->", Recipe.objects.all())
    # print("recipe objects 0 -------------->", Recipe.objects.all()[0].categories.all())

    matching_recipes = Recipe.objects.filter(categories__name__icontains=category.name)

    if matching_recipes.exists():
        recipes_found = True
    else:
        recipes_found = False

    context = {
        "category": category,
        "recipes_found": recipes_found,
        "matching_recipes": matching_recipes,
        "message": message,
    }

    print("context ---------------->", context)
    return render(request, "recipe/category.html", context)


def rate(request, recipe_slug, rating):
    recipe = Recipe.objects.get(slug=recipe_slug)
    Rating.objects.filter(post=recipe, user=request.user).delete()
    recipe.rating_set.create(user=request.user, rating=rating)
    return detail(request)
