from django.urls import path
from django.views.generic import RedirectView
from .views import UserListView, UserStatusToggleView, PostListView, PostDeleteView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='mondongo_user_list', permanent=False), name='mondongo_dashboard'),
    path('usuarios/', UserListView.as_view(), name='mondongo_user_list'),
    path('usuarios/<int:pk>/toggle/', UserStatusToggleView.as_view(), name='mondongo_user_toggle'),
    path('posteos/', PostListView.as_view(), name='mondongo_post_list'),
    path('posteos/<int:pk>/eliminar/', PostDeleteView.as_view(), name='mondongo_post_delete'),
]
