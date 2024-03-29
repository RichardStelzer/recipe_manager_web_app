"""recipe_manager_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path

from core.views import shortlist, search, about, frontpage, signup

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", signup, name="signup"),
    path("login/", views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("shortlist/", shortlist, name="shortlist"),
    path("search/", search, name="search"),
    path("about/", about, name="about"),
    path("", include("recipe.urls")),
    path("", frontpage, name="frontpage"),
]
