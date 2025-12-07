from django.contrib import admin
from .models import User, Post, Profile

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'status']
    list_filter = ['status']
    search_fields = ['username', 'email']

admin.site.register(User, UserAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['author', 'created_at']
    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'status']
    list_filter = ['status']
    search_fields = ['user__username']

admin.site.register(Profile, ProfileAdmin)
