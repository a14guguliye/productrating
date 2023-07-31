from django.db import models

# Create your models here.


class Product(models.Model):
    barcode=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
