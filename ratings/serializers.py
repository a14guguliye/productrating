from rest_framework import serializers
from .models import Ratings,AverageRating
from users.models import CustomUser
from products.models import Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','email','first_name','last_name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['description', 'barcode']



class RatingsSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    product=ProductSerializer() 
    class Meta:
        model=Ratings
        fields=['product','rating','user']



class RatingsPerProductSerializer(serializers.Serializer):
    product=serializers.CharField()
    rating=serializers.CharField()

    

    

