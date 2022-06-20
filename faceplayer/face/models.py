from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserOfApp(AbstractUser):
    uaddr= models.CharField(max_length=100, default='')
    zip= models.CharField(max_length=6, default=000000)
    state= models.CharField(max_length=100, default='x')
    city= models.CharField(max_length=100, default='x')
    phone= models.CharField(max_length=10, default='0000000000')
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.CharField(max_length=500, default='')
    spotify_uid = models.CharField(max_length=500, default='')
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email
