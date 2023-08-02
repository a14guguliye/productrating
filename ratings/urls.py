from django.urls import path
from .views import RatingsListView, RatingsSubmitPostView, RatingPerProductGetView


urlpatterns = [
    path("", RatingsListView.as_view()),
    path("newrating", RatingsSubmitPostView.as_view()), 
    path("perproduct", RatingPerProductGetView.as_view())
]
