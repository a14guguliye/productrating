from django.shortcuts import render
from rest_framework.views import APIView
from .models import Ratings
from .serializers import RatingsPerProductSerializer, RatingsSerializer
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from users.models import CustomUser
from .models import Ratings, AverageRating 
from products.models import Product
# Create your views here.




class RatingsListView(APIView):
    def get(self, *args, **kwargs):
        try:
            allRatings=Ratings.getAllRatings()
            allRatingsSerialized=RatingsSerializer(allRatings, many=True)
            return Response(allRatingsSerialized.data)
        except Exception as e:
           raise APIException(detail=str(e))
    


class RatingsSubmitPostView(APIView):
    def post(self,request,  *args, **kwargs):
        try:
            phoneId=request.data.get('phoneid')
            rating=request.data.get('rating')
            barcode=request.data.get('barcode')
            location=request.data.get('location')
            username=request.data.get("username")
            user=None 
            if(username):
                user=CustomUser.getUserByUsername(username=username)
            product=Product.getProductByBarcode(barcode=barcode)
            if(product is None):
                product=Product.objects.create(barcode=barcode, description="to be populated")
                product.save(); 
            newRating=Ratings.createNewRating(user=user, rating=rating,product=product, location=location, phoneId=phoneId)

            ratingSerializer=RatingsSerializer(newRating)
            return Response(ratingSerializer.data)
        except Exception as e:
            raise APIException(detail=str(e))
        


class RatingPerProductGetView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            barcode=request.data.get('barcode')

            averageRating=Ratings.getAverageRating(barcode=barcode)
            product=Product.getProductByBarcode(barcode=barcode)
    
            newAverageRatingSerialized=RatingsPerProductSerializer(data={"product":product.description, 
                                                                   "rating":str(averageRating)}
                                                                  )
            
            if(newAverageRatingSerialized.is_valid()):
                return Response(newAverageRatingSerialized.data)
            raise APIException(detail=str("invalid serializer"))
        except Exception as e:
            raise APIException(detail=str(e))

    def getProductByBarcode(self, barcode):
        return Product.objects.get(barcode=barcode)










