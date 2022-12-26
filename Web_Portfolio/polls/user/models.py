from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

class User(AbstractBaseUser):
    profile_img = models.TextField()
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=24,unique=True)

    USERNAME_FIELD = 'nickname'

    class Meta:
        db_table = 'User'
