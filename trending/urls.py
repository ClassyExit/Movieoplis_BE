from django.urls import path
from .views import TrendingAPI

urlpatterns = [
    path('trending', TrendingAPI.as_view(), name='trending')
]
