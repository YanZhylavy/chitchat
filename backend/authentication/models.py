from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, password=None,**fields):
        user = self.model(**fields)
        user.set_password(password)
        user.save()
        return user
    

class CustomUser(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField()
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    USERNAME_FIELD = "username"
    
    objects = CustomUserManager()