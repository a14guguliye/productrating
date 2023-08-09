from django.db import models
from products.models import Product
from users.models import CustomUser
# Create your models here.




class AverageRating(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    rating=models.CharField(max_length=20)

    class Meta:
        abstract=True 

class Ratings(models.Model):

    # CHOICES = [
    #     ('1', '1 star'),
    #     ('2', '2 stars'),
    #     ('3', '3 stars'),
    #     ('4', '4 stars'), 
    #     ('5', '5 stars'), 
    # ]
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    rating=models.CharField(max_length=20, blank=True, null=True)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE,  blank=True, null=True)
    phoneId=models.CharField(max_length=50, blank=True, null=True)
    location=models.CharField(max_length=50, blank=True, null=True)


    def __str__(self) -> str:
        return self.product.barcode
    
    class Meta:
        unique_together = (('product', 'user'),('product', 'phoneId'))


    @staticmethod
    def getAllRatings():
        return Ratings.objects.all() 
    
    @staticmethod
    def createNewRating(user:CustomUser, product:Product, rating:str, location:str, phoneId:str):
        newRating=Ratings.objects.create(user=user, rating=rating,product=product, location=location, phoneId=phoneId)
        newRating.save()
        return newRating
    
    @staticmethod
    def getAverageRating(barcode:str):
        ratings=Ratings.objects.filter(product=Product.objects.get(barcode=barcode))
        S=0.0
        for rating in ratings:
            S=S+float(rating.rating)
        try:
            return S/len(ratings)
        except ZeroDivisionError:
            return "0.0"
    



    
