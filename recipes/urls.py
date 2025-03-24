from . import views
from django.urls import path, include
from .views import RecipeListView, RecipeCreateView


app_name = 'recipes'
urlpatterns = [
    path('', views.index, name='home'),
    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('recipes/create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipes/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
]
