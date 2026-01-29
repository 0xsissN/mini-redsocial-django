from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile
from posts.models import Post, Reaction, Comment
from follows.models import Follow
from .models import Notification

class NotificationSignalTests(TestCase):
    def setUp(self):
        # Create users
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.profile1 = self.user1.profile
        self.profile2 = self.user2.profile
        
        # User2 follows User1
        Follow.objects.create(follower=self.profile2, following=self.profile1)

    def test_post_notification(self):
        # User1 creates a post
        post = Post.objects.create(author=self.profile1, content='Hello World')
        
        # User2 should receive a notification
        notification = Notification.objects.filter(user=self.profile2, notification_type='post').first()
        self.assertIsNotNone(notification)
        self.assertEqual(notification.sender, self.profile1)
        self.assertEqual(notification.post, post)

    def test_like_notification(self):
        post = Post.objects.create(author=self.profile1, content='Hello World')
        
        # User2 likes User1's post
        Reaction.objects.create(user=self.profile2, post=post, type='like')
        
        # User1 should receive a notification
        notification = Notification.objects.filter(user=self.profile1, notification_type='like').first()
        self.assertIsNotNone(notification)
        self.assertEqual(notification.sender, self.profile2)
        self.assertEqual(notification.post, post)

    def test_comment_notification(self):
        post = Post.objects.create(author=self.profile1, content='Hello World')
        
        # User2 comments on User1's post
        Comment.objects.create(author=self.profile2, post=post, content='Nice post!')
        
        # User1 should receive a notification
        notification = Notification.objects.filter(user=self.profile1, notification_type='comment').first()
        self.assertIsNotNone(notification)
        self.assertEqual(notification.sender, self.profile2)
        self.assertEqual(notification.post, post)
        
    def test_follow_notification(self):
        # User1 follows User2
        Follow.objects.create(follower=self.profile1, following=self.profile2)
        
        # User2 should receive a notification
        notification = Notification.objects.filter(user=self.profile2, notification_type='follow').first()
        self.assertIsNotNone(notification)
        self.assertEqual(notification.sender, self.profile1)

    def test_no_self_notification_like(self):
        post = Post.objects.create(author=self.profile1, content='Hello World')
        
        # User1 likes their own post
        Reaction.objects.create(user=self.profile1, post=post, type='like')
        
        # Should NOT receive a notification
        notification = Notification.objects.filter(user=self.profile1, notification_type='like').count()
        self.assertEqual(notification, 0)

    def test_no_self_notification_comment(self):
        post = Post.objects.create(author=self.profile1, content='Hello World')
        
        # User1 comments on their own post
        Comment.objects.create(author=self.profile1, post=post, content='My own comment')
        
        # Should NOT receive a notification
        notification = Notification.objects.filter(user=self.profile1, notification_type='comment').count()
        self.assertEqual(notification, 0)
