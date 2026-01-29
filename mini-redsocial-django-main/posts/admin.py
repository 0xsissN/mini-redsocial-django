from django.contrib import admin
from .models import Post, Reaction, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created_at')
    search_fields = ('content',)
    list_filter = ('created_at',)

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'type')
    search_fields = ('type',)
    list_filter = ('type',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'created_at')
    search_fields = ('content',)
    list_filter = ('created_at',)
