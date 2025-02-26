from django.urls import path
from .views import PopularMoviesAPI, MovieDetailsAPI


urlpatterns = [
    # Movie Lists
    path('movie/popular', PopularMoviesAPI.as_view(), name='movie-popular'),
    # Movie
    path('movie/details', MovieDetailsAPI.as_view(), name='movie-details'),   
]
