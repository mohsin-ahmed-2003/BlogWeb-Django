from django.contrib import admin
from blog.models import (
    Blog,
    Author,

)
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display= [
        'first_name',
        'last_name'
    ]

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display=[
       # 'author',
        'category',
        'title',
        'blog_image',
        'created_at',
    ]