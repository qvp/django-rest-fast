from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=160)
    text = models.TextField()
    photo = models.ImageField(upload_to='posts')
