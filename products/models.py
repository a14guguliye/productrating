from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.


class Product(models.Model):
    barcode=models.CharField(max_length=100, unique=True)
    description=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.barcode
    
    @staticmethod
    def getProductByBarcode(barcode:str):
        try:
            return Product.objects.get(barcode=barcode)
        except ObjectDoesNotExist:
            return None; 

