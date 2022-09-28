from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Cocktail


class CocktailsList(ListView):
    context_object_name = "cocktails"
    model = Cocktail
    queryset = Cocktail.objects.filter(status=1).order_by("title")
    template_name = "index.html"
