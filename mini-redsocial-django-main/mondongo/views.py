from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views.generic import ListView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from accounts.models import Profile
from posts.models import Post

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

class UserListView(AdminRequiredMixin, ListView):
    model = Profile
    template_name = 'mondongo/user_list.html'
    context_object_name = 'profiles'
    paginate_by = 14
    ordering = ['-user__date_joined']

    def get_queryset(self):
        queryset = super().get_queryset()
        
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(user__username__icontains=q) | 
                Q(bio__icontains=q)
            )
            
        status = self.request.GET.get('status')
        if status == 'active':
            queryset = queryset.filter(user__is_active=True)
        elif status == 'inactive':
            queryset = queryset.filter(user__is_active=False)
            
        return queryset

class UserStatusToggleView(AdminRequiredMixin, View):
    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if user == request.user:
            messages.error(request, 'No puedes desactivar tu propia cuenta.')
            return redirect('mondongo_user_list')
            
        user.is_active = not user.is_active
        user.save()
        status = "activado" if user.is_active else "desactivado"
        messages.success(request, f'Usuario {user.username} {status} correctamente.')
        return redirect('mondongo_user_list')

class PostListView(AdminRequiredMixin, ListView):
    model = Post
    template_name = 'mondongo/post_list.html'
    context_object_name = 'posts'
    paginate_by = 9
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(content__icontains=q) | 
                Q(author__user__username__icontains=q)
            )
            
        date = self.request.GET.get('date')
        if date:
            queryset = queryset.filter(created_at__date=date)
            
        return queryset

class PostDeleteView(AdminRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('mondongo_post_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Post eliminado correctamente.')
        return super().delete(request, *args, **kwargs)
