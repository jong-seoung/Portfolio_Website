from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from datetime import datetime
from django.utils.dateformat import DateFormat
today = DateFormat(datetime.now()).format('Y-m-d')

class UserManager(BaseUserManager):
    def create_user(self, email, name, nickname, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name = name,
            nickname = nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, nickname, password):
        user = self.create_user(
            email,
            name = name,
            nickname = nickname,
            password=password,
        )
        user.profile_img = "default_profile.png"
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    profile_img = models.TextField()
    name = models.CharField(max_length=24)
    nickname = models.CharField(max_length=24,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','nickname']
    

    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin