from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

# from django.views.generic.edit import *
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import redirect
from .models import Recipe, Comment, Like
from .forms import RecipeForm, CommentForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

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
    if request.user.is_superuser:
        recipe = get_object_or_404(Recipe, slug=slug)
    else:
        recipe = get_object_or_404(Recipe, slug=slug, is_published=1)
    liked_bakers = [like.baker for like in recipe.likes.all()]
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.baker = request.user.baker
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Comment submitted and awaiting approval"
            )
            return redirect("recipes:recipe_detail", slug=slug)

    return render(
        request,
        "recipes/recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "liked_bakers": liked_bakers,
        },
    )


@login_required
def like(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == "POST":

        # Use get_or_create which returns a tuple containing object and bool
        # (the bool specified whether something was creatd by this request)
        like, created = Like.objects.get_or_create(
            recipe=recipe,
            baker=request.user.baker,
        )
        if created:
            messages.success(request, "You have liked this recipe!")
        if not created:
            like.delete()
            messages.success(request,
            "You have removed your like from this recipe!")
        return redirect("recipes:recipe_detail", slug=slug)
    else:
        return HttpResponseBadRequest("Invalid request method.")


def comment_edit(request, slug, comment_id):
    #  view to edit comments
    queryset = Recipe.objects.filter(is_published=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and (
            comment.baker == request.user.baker or request.user.is_superuser
        ):
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.success(request, "Comment Updated!")
            return HttpResponseRedirect(reverse("recipes:recipe_detail", args=[slug]))
        else:
            messages.error(request, "Error updating comment. Please check your input.")
            return render(
                request,
                "recipes/recipe_detail.html",
                {
                    "comment_form": comment_form,
                    "recipe": recipe,
                    "comment": comment,
                },
            )

    else:  # Handle GET request implicity (maybe make this explicit?)
        comment_form = CommentForm(instance=comment)
        return render(
            request,
            "recipes/recipe_detail.html",
            {
                "comment_form": comment_form,
                "recipe": recipe,
                "comment": comment,
            },
        )


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
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.baker == request.user.baker or request.user.is_superuser:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment Deleted!")
    else:
        messages.add_message(request, messages.ERROR, "Error deleting comment!")
    return HttpResponseRedirect(reverse("recipes:recipe_detail", args=[slug]))



def index(request):
    return render(request, 'recipes/index.html')
