from django.urls import path
from .views import (
    FeedView, PostCreateView, PostUpdateView, PostDeleteView, 
    PostDetailView, CommentCreateView, toggle_like
)

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/like/', toggle_like, name='toggle_like'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
]
