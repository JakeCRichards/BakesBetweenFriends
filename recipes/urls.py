from django.urls import path
from .views import RecipeListView, RecipeCreateView

app_name = 'recipes'
urlpatterns = [
    path('', RecipeListView.as_view(), name='recipes'),
    path('create/', RecipeCreateView.as_view(), name='recipe_create'),
]
