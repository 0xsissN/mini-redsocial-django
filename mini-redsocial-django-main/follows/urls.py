from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.follow_user, name='follow_user'),
    path('dejar/<int:pk>/', views.unfollow_user, name='unfollow_user'),
]