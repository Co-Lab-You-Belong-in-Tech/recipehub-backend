from django.contrib import admin

from .models import UserProfile, UserInterest, UserRecipes

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserInterest)
admin.site.register(UserRecipes)