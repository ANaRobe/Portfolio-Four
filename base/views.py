from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from .models import Cocktail
from .forms import CocktailForm
from django.http import HttpResponseRedirect


def search_cocktails(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        cocktails = Cocktail.objects.filter(title__icontains=searched)
        return render(request, 'search_cocktails.html', {'searched':searched, 'cocktails':cocktails})
    
    else:
        return render(request, 'search_cocktails.html', {'searched':searched, 'cocktails':cocktails})


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
                "liked": liked,
            },
        )


class CocktailCreate(CreateView):
    template_name = 'edit.html'
    form_class = CocktailForm


class CocktailEdit(UpdateView):
    template_name = 'edit.html'
    form_class = CocktailForm
    queryset = Cocktail.objects.filter(status=1)


class CocktailDelete(DeleteView):
    model = Cocktail
    template_name = 'cocktail_confirm_delete.html'
    queryset = Cocktail.objects.filter(status=1)
    success_url = reverse_lazy('home')


class CocktailLike(View):

    def post(self, request, slug):
        cocktail = get_object_or_404(Cocktail, slug=slug)

        if cocktail.likes.filter(id=request.user.id).exists():
            cocktail.likes.remove(request.user)
        else:
            cocktail.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('cocktail', args=[slug]))

