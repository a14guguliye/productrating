from django.urls import path
from .views import RatingsListView


urlpatterns = [
    path("", RatingsListView.as_view()),
]
