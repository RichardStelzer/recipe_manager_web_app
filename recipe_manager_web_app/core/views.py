from django.shortcuts import render

from recipe.models import Recipe


def frontpage(request):
    recipes = Recipe.objects.all()
    return render(request, "core/frontpage.html", {"recipes": recipes})


def about(request):
    return render(request, "core/about.html")

