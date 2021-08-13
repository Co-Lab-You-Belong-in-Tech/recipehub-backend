from django.db import models

# Create your models here.
class myRecipes(models.Model):
    title = models.CharField(max_length = 120)
    link = models.URLField(max_length = 200)