from django.views.generic import ListView
from .models import Post

class FeedView(ListView):
    model = Post
    template_name = 'posts/feed.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
