from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from .forms import CreateUserForm


# Create your views here.
def homepage_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1> RecipeHub </h1>")   # string of HTML code
    return render(request, "homepage.html", {})


def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})


def register_view(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, "register.html", {'form': form})


class ProfileView(TemplateView):
    template_name = "profile.html"


class RecipeView(TemplateView):
    template_name = "recipelist.html"