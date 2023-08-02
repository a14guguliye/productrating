from django.shortcuts import render
from rest_framework.views import APIView
from .models import Ratings
from .serializers import RatingsSerializer
from rest_framework.response import Response
# Create your views here.




class RatingsListView(APIView):
    def get(self, *args, **kwargs):
        allRatings=Ratings.getAllRatings()
        allRatingsSerialized=RatingsSerializer(allRatings, many=True)
        return Response(allRatingsSerialized.data)

