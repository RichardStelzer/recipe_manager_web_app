from django.shortcuts import get_object_or_404, render

from .models import Recipe


def detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, "recipe/detail.html", {"recipe": recipe})
