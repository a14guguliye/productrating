from django.db import models
from products.models import Product
from users.models import CustomUser
# Create your models here.


class Ratings(models.Model):

    CHOICES = [
        ('1', '1 star'),
        ('2', '2 stars'),
        ('3', '3 stars'),
        ('4', '4 stars'), 
        ('5', '5 stars'), 
    ]
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    rating=models.CharField(max_length=20, choices=CHOICES, blank=True, null=True)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
