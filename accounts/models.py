from django.db import models

class Profile(models.Model):
    bio = models.TextField()

    avatar = models.ImageField(upload_to='media/avatars')
    birth_date = models.DateField()

    def __str__(self):
        return self.bio