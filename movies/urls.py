from django.urls import path
from .views import MovieCreditsAPI, MovieRecommendationsAPI, SimilarMoviesAPI, PopularMoviesAPI, UpcomingMoviesAPI, MovieDetails

urlpatterns = [
    path('movie/credits', MovieCreditsAPI.as_view(), name='movie-credits'),
    path('movie/recommendations', MovieRecommendationsAPI.as_view(),
         name='movie-recommendations'),
    path('movie/similar', SimilarMoviesAPI.as_view(), name='movie-similar'),
    path('movie/popular', PopularMoviesAPI.as_view(), name='movie-popular'),
    path('movie/upcoming', UpcomingMoviesAPI.as_view(), name='movie-upcoming'),
    path('movie/details', MovieDetails.as_view(), name='movie-details')
]
