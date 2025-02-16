from django.urls import path
from .views import TrendingAPI, TopRatedAPI, UpcomingMoviesAPI, NowPlayingMoviesAPI

urlpatterns = [
    path('trending', TrendingAPI.as_view(), name='trending'),
    path('top-rated', TopRatedAPI.as_view(), name='top-rated'),
    path('upcoming', UpcomingMoviesAPI.as_view(), name='upcoming'),
    path('now-playing', NowPlayingMoviesAPI.as_view(), name='nowplaying'),
]
