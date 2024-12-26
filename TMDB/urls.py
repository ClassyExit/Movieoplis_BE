from django.urls import path

from .views import TVGenreAPI, MovieGenreAPI, StatusPageAPI

urlpatterns = [
    path('tv/genre', TVGenreAPI.as_view(), name='genre-tv'),
    path('movie/genre', MovieGenreAPI.as_view(), name='genre-movie'),
    path('health', StatusPageAPI.as_view(), name='status'),
    
]
