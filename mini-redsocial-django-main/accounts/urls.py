from django.urls import path
from . import views
from .views import ProfileDetailView

urlpatterns = [
    path('perfil/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('editar/', views.edit_profile, name='profile-edit'),
]
