"""recipehub URL Configuration

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
from django.urls import path

from pages.views import homepage_view, login_view, register_view, ProfileView, RecipeView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', homepage_view, name='home'),
    path('myrecipes/', RecipeView.as_view(), name='myrecipes'),
    path('admin/', admin.site.urls),
    path('profile/', ProfileView.as_view(), name='profile'),

    # Django Auth
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register')
]
