from django.db.models.signals import post_save
from django.dispatch import receiver
from posts.models import Post, Reaction, Comment
from follows.models import Follow
from .models import Notification

@receiver(post_save, sender=Post)
def create_post_notification(sender, instance, created, **kwargs):
    if created:
        followers = instance.author.following.all()
        for follow in followers:
            Notification.objects.create(
                user=follow.follower,
                sender=instance.author,
                post=instance,
                notification_type='post'
            )

@receiver(post_save, sender=Reaction)
def create_like_notification(sender, instance, created, **kwargs):
    if created and instance.type == 'like':
        if instance.user != instance.post.author:
            Notification.objects.create(
                user=instance.post.author,
                sender=instance.user,
                post=instance.post,
                notification_type='like'
            )

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        if instance.author != instance.post.author:
            Notification.objects.create(
                user=instance.post.author,
                sender=instance.author,
                post=instance.post,
                notification_type='comment'
            )

@receiver(post_save, sender=Follow)
def create_follow_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.following,
            sender=instance.follower,
            notification_type='follow'
        )
