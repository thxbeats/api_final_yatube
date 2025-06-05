from django.contrib import admin

from .models import Group, Post, Comment, Follow


# Register your models here.
@admin.register(Group, Post, Comment, Follow)
class CustomAdmin(admin.ModelAdmin):
    pass
