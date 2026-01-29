from django.views.generic import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import ProfileUpdateForm
from posts.models import Post
from follows.models import Follow

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        
        posts = Post.objects.filter(author=profile).order_by('-created_at')
        context['posts'] = posts
        context['posts_count'] = posts.count()
        context['followers_count'] = profile.followers.count()
        context['following_count'] = profile.following.count()
        
        # Check if current user is following this profile
        if self.request.user.is_authenticated:
            context['is_following'] = Follow.objects.filter(
                follower=self.request.user.profile,
                following=profile
            ).exists()
        else:
            context['is_following'] = False
        
        return context

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Perfil actualizado con éxito!')
            return redirect('profile-edit')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request, 'accounts/profile_edit.html', {'form': form})
