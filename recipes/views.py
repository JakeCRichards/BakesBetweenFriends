from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm
from django.utils.text import slugify

# Create your views here.


class RecipeListView(generic.ListView):
    queryset = Recipe.objects.filter(is_published=True)
    template_name = 'recipes/recipe_list.html'
    paginate_by = 6


class RecipeCreateView(generic.CreateView):
    model = Recipe
    template_name = 'recipes/recipe_form.html'
    form_class = RecipeForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.baker = self.request.user.baker
        form.instance.slug = slugify(form.instance.title)
        # Add a message saying that the recipe has been submitted for approval
        messages.add_message(
            self.request, messages.SUCCESS,
            'Recipe submitted and awaiting approval'
        )
        return super().form_valid(form)


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.baker = request.user.baker
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
                )
    comment_form = CommentForm()        

    return render(request, 'recipes/recipe_detail.html', {
                'recipe': recipe,
                'comments': comments,
                'comment_count': comment_count,
                'comment_form': comment_form,
            })


def like(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    recipe.likes += 1
    recipe.save()
    messages.add_message(
                request, messages.SUCCESS,
                'You have liked this recipe'
                )
    return HttpResponseRedirect(recipe.get_absolute_url())


def comment_edit(request, slug, pk, comment_id):
    #  view to edit comments
    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.baker == request.user.baker:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
            messages.add_message(
                request, messages.ERROR, 
                'Error updating comment!'
            )
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete a comment associated with a recipe.

    Args:
        request: The HTTP request object.
        slug: The slug of the recipe.
        comment_id: The ID of the comment to be deleted.

    Returns:
        HttpResponseRedirect: Redirects to the recipe detail page.
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.baker == request.user.baker:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment Deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'Error deleting comment!')
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def index(request):
    return render(request, 'recipes/index.html')
