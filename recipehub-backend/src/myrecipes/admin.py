from django.contrib import admin

# Register your models here.
from .models import myRecipes

admin.site.register(myRecipes)