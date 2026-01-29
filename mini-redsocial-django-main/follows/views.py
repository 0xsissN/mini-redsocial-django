from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from accounts.models import Profile
from .models import Follow

@login_required
def follow_user(request, pk):
    profile_to_follow = Profile.objects.get(pk=pk)
    
    if request.user.profile != profile_to_follow:
        Follow.objects.get_or_create(
            follower=request.user.profile,
            following=profile_to_follow
        )
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'followers_count': profile_to_follow.followers.count(),
                'following_count': request.user.profile.following.count(),
                'is_following': True
            })
        else:
            messages.success(request, f'Ahora sigues a {profile_to_follow.user.username}')
    
    return redirect('profile_detail', pk=pk)

@login_required
def unfollow_user(request, pk):
    profile_to_unfollow = Profile.objects.get(pk=pk)
    
    if request.user.profile != profile_to_unfollow:
        Follow.objects.filter(
            follower=request.user.profile,
            following=profile_to_unfollow
        ).delete()
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'followers_count': profile_to_unfollow.followers.count(),
                'following_count': request.user.profile.following.count(),
                'is_following': False
            })
        else:
            messages.success(request, f'Ya no sigues a {profile_to_unfollow.user.username}')
    
    return redirect('profile_detail', pk=pk)
