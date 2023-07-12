from django.contrib import admin
from .models import Podcast, Category, Tag, Comment, Season, Like

admin.site.register(Season)
admin.site.register(Like)


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'category', 'created_date']
    list_filter = ['tag', 'category']
    date_hierarchy = 'created_date'
    filter_horizontal = ['tag']
    search_fields = ['author', 'title']


@admin.register(Category)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']





@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'podcast', 'author', 'created_date']
    date_hierarchy = 'created_date'
    search_fields = ['podcast', 'article__title', 'author_username', 'author__first_name', 'author__last_name']
    autocomplete_fields = ['author', 'podcast']

