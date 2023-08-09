from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    
    profile_image = models.TextField(default='')  # profile image
    nickname = models.CharField(max_length=24, unique=True, default='')
    name = models.CharField(max_length=24, default='')
    email = models.EmailField(unique=True, default='')

    USERNAME_FIELD = 'nickname'

    class Meta:
        db_table = 'User'
