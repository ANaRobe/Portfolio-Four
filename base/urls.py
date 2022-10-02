from .views import CocktailsList, CocktailDetail, CocktailCreate
from django.urls import path

urlpatterns = [
    path('', CocktailsList.as_view(), name='home'),
    path('<slug:slug>/', CocktailDetail.as_view(), name='cocktail'),
    path('add', CocktailCreate.as_view(), name='add'),
]