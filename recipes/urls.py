from . import views
from django.urls import path
from .views import RecipeListView, RecipeCreateView, RecipeCategoryListView, RecipeUpdateView


app_name = 'recipes'
urlpatterns = [
    path('', views.index, name='home'),
    path('baker/<str:username>/', views.baker_profile, name='baker_profile'),
    path('baker/<str:username>/edit/', views.edit_baker_profile,
         name='edit_baker_profile'),
    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('recipes/categories/',
         RecipeCategoryListView.as_view(), name='categories'),
    path('recipes/create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipes/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/<slug:slug>/edit/', RecipeUpdateView.as_view(), name='recipe_edit'),
    path('recipes/<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('recipes/<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('recipes/<slug:slug>/like/', views.like, name='add_remove_like'),
]
