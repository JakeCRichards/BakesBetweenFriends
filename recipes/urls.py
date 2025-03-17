from . import views
from django.urls import path, include
from .views import RecipeListView, RecipeCreateView


app_name = 'recipes'
urlpatterns = [
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('', RecipeListView.as_view(), name='recipes'),
    path('create/', RecipeCreateView.as_view(), name='recipe_create'),   
]
