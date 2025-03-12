from . import views
from django.urls import path, include

app_name = 'recipes'
urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipe_list'),
    path('create/', views.RecipeCreateView.as_view(), name='recipe_create'),
]
