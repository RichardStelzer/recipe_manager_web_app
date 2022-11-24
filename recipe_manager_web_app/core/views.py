from django.shortcuts import render
from django.http import Http404

from recipe.models import Recipe

from django.db.models import Q


def shortlist(request):
    recipes = Recipe.objects.all()
    print("recipes", recipes)
    return render(request, "core/shortlist.html", {"recipes": recipes})


def search(request):
    search_query = request.GET.get("q")

    if search_query is None or search_query == "":
        message = "You submitted nothing!"
        recipes_found = False
        search_result = None
    else:
        message = "Search results for \'" + str(search_query) + "\'"
        search_result = Recipe.objects.filter(Q(title__icontains=search_query) |
                                              Q(brief_description__icontains=search_query) |
                                              Q(full_description__icontains=search_query) |
                                              Q(author__icontains=search_query))

        if search_result.exists():
            recipes_found = True
        else:
            recipes_found = False

    return render(request, "core/search.html", {"search_result": search_result,
                                                "recipes_found": recipes_found,
                                                "message": message})


def frontpage(request):
    recipes = Recipe.objects.all()
    return render(request, "core/frontpage.html", {"recipes": recipes})


def about(request):
    return render(request, "core/about.html")

