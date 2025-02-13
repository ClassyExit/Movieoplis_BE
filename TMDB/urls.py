from django.urls import path

from .views import  StatusPageAPI, GenreAPI

urlpatterns = [
    path('genre', GenreAPI.as_view(), name='genres'),
    path('health', StatusPageAPI.as_view(), name='status'),
    
]
