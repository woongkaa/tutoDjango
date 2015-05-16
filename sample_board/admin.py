from django.contrib import admin
from sample_board.models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'created']
    list_editable = ['name']
    search_fields = ['name']
    ordering = ['name']

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created']
    list_filter = ['category']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content', ]
    ordering = ['created']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)