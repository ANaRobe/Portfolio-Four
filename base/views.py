from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from .models import Cocktail
from .forms import CocktailForm, RemarkForm
from django.http import HttpResponseRedirect
from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


def search_cocktails(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        cocktails = Cocktail.objects.annotate(search=SearchVector('title', 'ingredients'),).filter(search=searched)
        return render(request, 'search_cocktails.html', {'searched': searched, 'cocktails': cocktails})

    else:
        return render(request, 'search_cocktails.html', {'searched': searched, 'cocktails': cocktails})


class CocktailsList(ListView):
    context_object_name = "cocktails"
    model = Cocktail
    queryset = Cocktail.objects.filter(status=1).order_by("title")
    template_name = "index.html"


class CocktailDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Cocktail.objects.filter(status=1)
        cocktail = get_object_or_404(queryset, slug=slug)
        remarks = cocktail.remarks.order_by("publish_date")
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
                "remark_form": RemarkForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Cocktail.objects.filter(status=1)
        cocktail = get_object_or_404(queryset, slug=slug)
        remarks = cocktail.remarks.order_by("publish_date")
        liked = False
        if cocktail.likes.filter(id=self.request.user.id).exists():
            liked = True

        remark_form = RemarkForm(data=request.POST)

        if remark_form.is_valid():
            remark_form.instance.user = request.user
            remark = remark_form.save(commit=False)
            remark.cocktail = cocktail
            remark.save()
            messages.success(request, 'Successfully Remarked')
        else:
            remark_form =RemarkForm()
            messages.error(request, 'Sorry! We were not able to post this remark. Try again!')

        return render(
            request,
            "cocktail.html",
            {
                "cocktail": cocktail,
                "remarks": remarks,
                "liked": liked,
                "remark_form": RemarkForm()
            },
        )


class CocktailCreate(SuccessMessageMixin, CreateView):
    template_name = 'edit.html'
    form_class = CocktailForm
    success_url = reverse_lazy('home')
    success_message = 'Successfully Added New Cocktail'


class CocktailEdit(SuccessMessageMixin, UpdateView):
    template_name = 'edit.html'
    form_class = CocktailForm
    queryset = Cocktail.objects.filter(status=1)
    success_message = 'Successfully Updated Cocktail'


class CocktailDelete(SuccessMessageMixin, DeleteView):
    model = Cocktail
    template_name = 'cocktail_confirm_delete.html'
    queryset = Cocktail.objects.filter(status=1)
    success_url = reverse_lazy('home')
    success_message = 'Successfully Removed Cocktail'


class CocktailLike(View):

    def post(self, request, slug):
        cocktail = get_object_or_404(Cocktail, slug=slug)

        if cocktail.likes.filter(id=request.user.id).exists():
            cocktail.likes.remove(request.user)
        else:
            cocktail.likes.add(request.user)
        return HttpResponseRedirect(reverse('cocktail', args=[slug]))


class UsersFavCocktails(View):

    def get(self, request):

        if request.user.is_authenticated:
            cocktails = Cocktail.objects.filter(likes=request.user.id)
            paginator = Paginator(cocktails, 6)  # Show 6 Recipes per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'favourites.html', {
                'page_obj': page_obj
                })
        else:
            return render(request, 'favourites.html')