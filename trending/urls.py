from django.urls import path
from .views import TrendingAPI, TopRatedAPI

urlpatterns = [
    path('trending', TrendingAPI.as_view(), name='trending'),
    path('top-rated', TopRatedAPI.as_view(), name='top-rated'),
]
