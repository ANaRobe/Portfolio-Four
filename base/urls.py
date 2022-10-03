from .views import CocktailsList, CocktailDetail, CocktailCreate, CocktailEdit
from django.urls import path

urlpatterns = [
    path('', CocktailsList.as_view(), name='home'),
    path('<slug:slug>/', CocktailDetail.as_view(), name='cocktail'),
    path('add/', CocktailCreate.as_view(), name='add'),
    path('edit/<slug:slug>/', CocktailEdit.as_view(), name='edit'),
]