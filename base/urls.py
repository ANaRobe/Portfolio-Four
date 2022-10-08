from .views import CocktailsList, CocktailDetail, CocktailCreate, CocktailEdit, CocktailDelete
from django.urls import path

urlpatterns = [
    path('', CocktailsList.as_view(), name='home'),
    path('add/', CocktailCreate.as_view(), name='add'),
    path('edit/<slug:slug>/', CocktailEdit.as_view(), name='edit'),
    path('delete/<slug:slug>/', CocktailDelete.as_view(), name='delete'),
    path('<slug:slug>/', CocktailDetail.as_view(), name='cocktail'),
]