from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Teacher','Teacher'),
        ('Student','Student'),
    )
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=100, null=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Book(models.Model):
    name = models.CharField(max_length=180)
    content = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name, self.owner
