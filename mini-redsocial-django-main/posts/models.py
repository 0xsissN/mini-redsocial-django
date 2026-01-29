from django.db import models
from accounts.models import Profile

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:30]
    
    def likes_count(self):
        return self.reactions.filter(type='like').count()
    
    def user_has_liked(self, profile):
        if not profile:
            return False
        return self.reactions.filter(user=profile, type='like').exists()

class Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, default='like')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('post', 'user', 'type')
    
    def __str__(self):
        return f"{self.user.user.username} - {self.type} - {self.post.id}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author.user.username}: {self.content[:30]}"