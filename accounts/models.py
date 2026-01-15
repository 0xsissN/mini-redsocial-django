from django.db import models

class Profile(models.Model):
    id = models.CharField(primary_key=True)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='media/avatars')
    birth_date = models.DateField()
