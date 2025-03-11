from django.contrib import admin
from .models import Recipe, Category, Comment, Like, Baker
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'is_published')
    search_fields = ['title']
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'instructions')


# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Baker)