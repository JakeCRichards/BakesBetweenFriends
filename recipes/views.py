from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic, View

# from django.views.generic.edit import *
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import redirect
from django.db import models
from django.db.models import Prefetch
from .models import Recipe, Comment, Like, Category, Baker
from .forms import RecipeForm, CommentForm, ProfileForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


class RecipeListView(generic.ListView):
    template_name = 'recipes/recipe_list.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = Recipe.objects.filter(is_published=True).annotate(
            comment_count=models.Count('comments', filter=models.Q(
                comments__approved=True))).order_by(
                    '-created_on')
        return queryset


class RecipeCreateView(generic.CreateView):
    model = Recipe
    template_name = 'recipes/recipe_form.html'
    form_class = RecipeForm

    def form_valid(self, form):
        form.instance.baker = self.request.user.baker
        form.instance.slug = slugify(form.instance.title)
        # Add a message saying that the recipe has been submitted for approval
        messages.add_message(
            self.request, messages.SUCCESS,
            f"{form.instance.title} Recipe submitted and awaiting approval"
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'recipes:recipe_detail',
            kwargs={"slug": self.object.slug}
        )


class RecipeUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView
):
    model = Recipe
    template_name = 'recipes/recipe_form.html'
    form_class = RecipeForm

    def test_func(self):
        return (
            self.request.user.is_superuser or
            self.request.user.baker == self.get_object().baker
        )

    def handle_no_permission(self):
        messages.error(
            self.request, "You do not have permission to edit this recipe"
        )
        return redirect("recipes:recipe_detail", slug=self.get_object().slug)

    def form_valid(self, form):
        form.instance.is_published = False
        # Add a message saying that the recipe has been updated
        # and is awaiting approval
        messages.add_message(
            self.request, messages.SUCCESS,
            f"{self.object.title} Recipe updated and awaiting approval"
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'recipes:recipe_detail',
            kwargs={"slug": self.object.slug}
        )

# superuser publish view to publish recipes


class RecipePublishView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self, slug):
        recipe = get_object_or_404(Recipe, slug=slug)
        messages.error(
            self.request,
            "You do not have permission to publish this recipe"
        )
        return redirect("recipes:recipe_detail", slug=recipe.slug)

    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)
        recipe.is_published = True
        recipe.save()
        messages.success(request, "Recipe published")
        return redirect("recipes:recipe_detail", slug=recipe.slug)


# psuedo delete view to unpublish recipes
class RecipeUnpublishView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return (
            self.request.user.is_superuser or
            self.request.user.baker == self.get_object().baker
        )

    def handle_no_permission(self, slug):
        recipe = get_object_or_404(Recipe, slug=slug)
        messages.error(
            self.request,
            "You do not have permission to unpublish this recipe"
        )
        return redirect("recipes:recipe_detail", slug=recipe.slug)

    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)
        recipe.is_published = False
        recipe.save()
        messages.success(request, "Recipe unpublished")
        return redirect("recipes:recipe_detail", slug=recipe.slug)


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    comment_count = recipe.comments.all().count()
    # if not request.user.is_superuser and request.user.baker != recipe.baker
    # and not recipe.is_published:
    if not (
        recipe.is_published or
        request.user.is_authenticated and (
            request.user.is_superuser or
            request.user.baker == recipe.baker
        )
    ):
        messages.error(request, "This recipe is not published yet.")
        return redirect("recipes:recipes")

    liked_bakers = [like.baker for like in recipe.likes.all()]
    if request.user.is_superuser:
        comments = recipe.comments.all().order_by("-created_on")
    else:
        comments = recipe.comments.filter(
            approved=True
        ).order_by("-created_on")
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
            return HttpResponseRedirect(reverse("recipes:recipe_detail",
                                                args=[slug]))
        else:
            messages.error(request,
                           "Error updating comment. Please check your input.")
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
                "edit_mode": True,
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
        messages.add_message(request, messages.ERROR,
                             "Error deleting comment!")
    return HttpResponseRedirect(reverse("recipes:recipe_detail", args=[slug]))


def index(request):
    return render(request, 'recipes/index.html')


class RecipeCategoryListView(generic.ListView):
    model = Recipe
    template_name = 'recipes/recipe_categories.html'
    # create a view that lists all the categories
    # and the recipes in each category as links

    def get_queryset(self):
        return Category.objects.prefetch_related(
            Prefetch('tags', queryset=Recipe.objects.filter(is_published=True))
        )

# View to see the baker profile page


def baker_profile(request, username):
    baker = get_object_or_404(Baker, user__username=username)
    recipes = Recipe.objects.filter(baker=baker, is_published=True)
    return render(
        request,
        'recipes/baker_profile.html',
        {
            'baker': baker,
            'recipes': recipes,
        }
    )

# Create edit of baker profile


@login_required
def edit_baker_profile(request, username):
    baker = get_object_or_404(Baker, user__username=username)
    if request.user != baker.user:
        messages.error(
            request,
            "You do not have permission to edit this profile"
        )
        return redirect("recipes:baker_profile", username=username)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=baker)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("recipes:baker_profile", username=username)
        else:
            messages.error(request, "Error updating profile")
    else:
        form = ProfileForm(instance=baker)
    return render(
        request,
        "recipes/profile_form.html",
        {
            "form": form,
            "baker": baker
        }
    )
