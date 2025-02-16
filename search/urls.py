from django.urls import path
from .views import  MultiSearchAPI


urlpatterns = [
    path('search', MultiSearchAPI.as_view(), name='search-multi'),    
]
