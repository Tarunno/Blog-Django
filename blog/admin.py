from django.contrib import admin
from . models import Category, Post, Comment

admin.site.site_header = "OUR WORDS | admin"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'date']
    list_filter = ['category', 'author']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'date']
    list_filter = ['user']
