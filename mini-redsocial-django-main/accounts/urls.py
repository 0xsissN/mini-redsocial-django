from django.urls import path
from . import views
from .views import ProfileDetailView

urlpatterns = [
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/edit/', views.edit_profile, name='profile-edit'),
]
