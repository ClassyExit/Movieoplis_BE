from django.urls import path

from .views import  StatusPageAPI, GenreAPI

urlpatterns = [
    path('genres', GenreAPI.as_view(), name='genres'),
    path('health', StatusPageAPI.as_view(), name='status'),
    
]
