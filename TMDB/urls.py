from django.urls import path

from .views import TVGenreAPI, MovieGenreAPI

urlpatterns = [
    path('tv/genre', TVGenreAPI.as_view(), name='genre-tv'),
    path('movie/genre', MovieGenreAPI.as_view(), name='genre-movie')
]
