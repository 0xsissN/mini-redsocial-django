from django.db import models
from accounts.models import Profile

class Post(models.Model):
    id = models.CharField(primary_key=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='media/posts', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Reaction(models.Model):
    id = models.CharField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    id = models.CharField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)