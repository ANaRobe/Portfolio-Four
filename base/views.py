from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views import View
from .models import Cocktail, Remark



class CocktailsList(ListView):
    context_object_name = "cocktails"
    model = Cocktail
    queryset = Cocktail.objects.filter(status=1).order_by("title")
    template_name = "index.html"


class CocktailDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Cocktail.objects.filter(status=1)
        cocktail = get_object_or_404(queryset, slug=slug)
        remarks = cocktail.remarks.filter(approved=True).order_by("publish_date")
        liked = False
        if cocktail.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "cocktail.html",
            {
                "cocktail": cocktail,
                "remarks": remarks,
                "liked": liked
            },
        )