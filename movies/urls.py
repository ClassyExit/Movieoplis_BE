from django.urls import path
from .views import PopularMoviesAPI, UpcomingMoviesAPI, MovieDetailsAPI, MovieTopRatedAPI, NowPlayingMoviesAPI


urlpatterns = [
    # Movie Lists
    path('movie/popular', PopularMoviesAPI.as_view(), name='movie-popular'),
    path('movie/upcoming', UpcomingMoviesAPI.as_view(), name='movie-upcoming'),
    path('movie/toprated', MovieTopRatedAPI.as_view(), name='movie-toprated'),
    path('movie/nowplaying', NowPlayingMoviesAPI.as_view(), name='movie-nowplaying'),

    # Movie
    path('movie/details', MovieDetailsAPI.as_view(), name='movie-details'),
    
]
 