from  .views import CocktailsList
from django.urls import path

urlpatterns = [
    path('', CocktailsList.as_view(), name='home'),
]