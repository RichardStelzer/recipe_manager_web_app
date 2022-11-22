from django.urls import path

from . import views

urlpatterns = [
    # https://docs.djangoproject.com/en/4.1/topics/http/urls/ section "Path converters"
    # <slug = django path converter,
    # :slug> = custom variable name passed to views.detail function "def detail(request, slug)"
    # <slug:slugtest> would work with "def detail(request, slugtest)"
    path("<slug:slug>/", views.detail, name="recipe_detail"),
]
