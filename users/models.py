from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)
    is_premium = models.BooleanField(default=False)

    class Meta:
        app_label = 'users'

    def __str__(self):
        return self.username