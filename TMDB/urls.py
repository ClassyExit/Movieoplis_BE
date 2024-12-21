from django.urls import path

from .views import TVGenreAPI, MovieGenreAPI

urlpatterns = [
    path('genre/tv', TVGenreAPI.as_view(), name='genre-tv'),
    path('genre/movie', MovieGenreAPI.as_view(), name='genre-movie')
]
