from django.db import models

# Create your models here.


class Product(models.Model):
    barcode=models.CharField(max_length=100, unique=True)
    description=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.barcode
