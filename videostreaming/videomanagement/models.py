from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Add custom fields if needed
    pass

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    video_url = models.URLField()

    def __str__(self):
        return self.name
