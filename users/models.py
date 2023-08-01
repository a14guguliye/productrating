from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    def __str__(self) -> str:
        return self.get_username
