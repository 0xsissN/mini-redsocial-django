from django.urls import path
from .views import (
    FeedView, PostCreateView, PostUpdateView, PostDeleteView, 
    PostDetailView, CommentCreateView, toggle_like
)

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    path('crear/', PostCreateView.as_view(), name='post_create'),
    path('detalle/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('editar/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('eliminar/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('megusta/<int:pk>/', toggle_like, name='toggle_like'),
    path('comentar/<int:pk>/', CommentCreateView.as_view(), name='comment_create'),
]
