from django.views.generic import DetailView
from .models import Profile

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['posts'] = profile.post_set.all().order_by('-created_at')
        context['followers_count'] = profile.followers.count()
        context['following_count'] = profile.following.count()
        context['posts_count'] = profile.post_set.count()
        return context
