from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Baker(models.Model):
    class UserTypes(models.TextChoices):
        PROFESSIONAL = 'professional', 'Professional'
        HOME_BAKER = 'home_baker', 'Home Baker'
        BEGINNER = 'beginner', 'Complete Beginner'
        HOPELESS = 'hopeless', 'Hopeless Baker'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='static/assets/images/profile_pics', blank=True)
    user_type = models.CharField(max_length=50, choices=UserTypes.choices, default=UserTypes.BEGINNER)
    

    def __str__(self):
        return f"Baker {self.user.username}"

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    baker = models.ForeignKey(Baker, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True,)
    image = models.ImageField(upload_to='static/assets/images/recipe_images')
    ingredients = models.TextField()
    instructions = models.TextField()
    time_required = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    categories = models.ManyToManyField('Category', related_name='tags')

    def __str__(self):
        return f"{self.title} by {self.baker.user.username}"
    
    class Meta:
        ordering = ['-created_on']


class Category(models.Model):
    class TagTypes(models.TextChoices):
        DIETARY = 'dietary', 'Dietary'
        ALLERGY = 'allergy', 'Allergy'
        CUISINE = 'cuisine', 'Cuisine'
    tag_name = models.CharField(max_length=50, unique=True)
    recipes = models.ManyToManyField(Recipe, blank=True)
    tag_type = models.CharField(max_length=50, choices=TagTypes.choices)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['tag_name']
    
    def __str__(self):
        return self.tag_name


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    baker = models.ForeignKey(Baker, on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.comment} by {self.baker.user.username}"
    
    class Meta:
        ordering = ['created_on']


class Like(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='likes')
    baker = models.ForeignKey(Baker, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Baker {self.baker.user.username} liked {self.recipe.title}"
    
    class Meta:
        ordering = ['created_on']