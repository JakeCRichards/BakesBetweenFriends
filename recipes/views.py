from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import *
from .models import Recipe, Comment

# Create your views here.

class RecipeListView(generic.ListView):
    queryset = Recipe.objects.filter(is_published=True)
    template_name = 'recipes/recipe_list.html'
    paginate_by = 6

class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['title', 'baker', 'slug', 'image', 'ingredients', 'instructions', 'time_required', 'is_published', 'categories']
    template_name = 'recipes/recipe_form.html'