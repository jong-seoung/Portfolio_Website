from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser



class User(AbstractBaseUser):
    profile_img = models.TextField()
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'User'
