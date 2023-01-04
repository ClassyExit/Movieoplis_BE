from django.urls import path
from .views import MovieReviewAPI, TVReviewAPI

urlpatterns = [
    path('movie/review', MovieReviewAPI.as_view(), name='movie-review'),
    path('tv/review', TVReviewAPI.as_view(), name='tv-review')
]
