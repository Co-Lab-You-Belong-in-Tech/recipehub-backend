from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInterest(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return (self.name)

class UserProfile(models.Model):
    # owner
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "profile")

    # setting
    is_full_name_displayed = models.BooleanField(default=True)

    # details
    bio = models.CharField(max_length=500, blank=True, null=True)
    interests = models.ManyToManyField(UserInterest, blank=True)

class UserRecipes(models.Model):
    title = models.CharField(max_length = 120)
    link = models.URLField(max_length = 200)
