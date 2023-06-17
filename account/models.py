from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValidationError('Please enter email')
        user = MyUser(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staff(self, email, password, fullname=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, fullname=None):
        user = self.create_staff(email, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    object = MyUserManager()

    def __str__(self):
        return self.email