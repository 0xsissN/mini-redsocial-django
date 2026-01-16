from django.contrib import admin
from .models import Post, Reaction, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created_at')
    search_fields = ('content', 'author__id')
    list_filter = ('created_at',)

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'created_at')
    search_fields = ('user__id', 'post__id')
    list_filter = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'created_at', 'is_active')
    search_fields = ('content', 'user__id', 'post__id')
    list_filter = ('created_at', 'is_active')
