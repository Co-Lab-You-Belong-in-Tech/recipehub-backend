from django.shortcuts import render

from .models import myRecipes

# Create your views here.
def myrecipes_detail_view(request):
    obj = myRecipes.objects.get(id=1)
    context = {
        "title": obj.title,
        "link": obj.link
    }
    return render(request, "myrecipes/detail.html", context)