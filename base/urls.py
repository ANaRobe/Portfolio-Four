from .views import CocktailsList, CocktailDetail, CocktailCreate, CocktailEdit, CocktailDelete, CocktailLike, search_cocktails
from django.urls import path

urlpatterns = [
    path('', CocktailsList.as_view(), name='home'),
    path('add/', CocktailCreate.as_view(), name='add'),
    path('search_cocktails/', search_cocktails, name='search_cocktails'),
    path('edit/<slug:slug>/', CocktailEdit.as_view(), name='edit'),
    path('delete/<slug:slug>/', CocktailDelete.as_view(), name='delete'),
    path('like/<slug:slug>', CocktailLike.as_view(), name='cocktail_like'),
    path('<slug:slug>/', CocktailDetail.as_view(), name='cocktail'),
]