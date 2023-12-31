from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

# Create your models here.
class CustomUser(AbstractUser):

    def __str__(self) -> str:
        return super().__str__()
    

    @staticmethod
    def getUserByUsername(username:str):
        return CustomUser.objects.get(username=username)
    
