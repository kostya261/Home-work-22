from django.contrib import admin

from blog.models import Topic, Article


# Register your models here.

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'topic', 'created_at', 'is_published', 'views']
    list_filter = ['topic', 'is_published', 'created_at']
    search_fields = ['title', 'content']
    date_hierarchy = 'created_at'