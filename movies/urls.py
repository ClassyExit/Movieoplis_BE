from django.urls import path
from .views import MovieCreditsAPI, MovieRecommendationsAPI, SimilarMoviesAPI, PopularMoviesAPI, UpcomingMoviesAPI, MovieDetailsAPI, MovieTopRatedAPI, NowPlayingMoviesAPI, MovieVideosAPI, MovieProvidersAPI


urlpatterns = [
    # Movie Lists
    path('movie/popular', PopularMoviesAPI.as_view(), name='movie-popular'),
    path('movie/upcoming', UpcomingMoviesAPI.as_view(), name='movie-upcoming'),
    path('movie/toprated', MovieTopRatedAPI.as_view(), name='movie-toprated'),
    path('movie/nowplaying', NowPlayingMoviesAPI.as_view(), name='movie-nowplaying'),


    # Movie
    path('movie/details', MovieDetailsAPI.as_view(), name='movie-details'),
    path('movie/recommendations', MovieRecommendationsAPI.as_view(),
         name='movie-recommendations'),
    path('movie/similar', SimilarMoviesAPI.as_view(), name='movie-similar'),
    path('movie/credits', MovieCreditsAPI.as_view(), name='movie-credits'), 
    path('movie/videos', MovieVideosAPI.as_view(), name='movie-videos'),
    path('movie/providers', MovieProvidersAPI.as_view(), name='movie-providers'),
]
