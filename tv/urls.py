from django.urls import path
from .views import TVDetailsAPI, TVPopularAPI, TVSeasonDetailsAPI, TVEpisodeDetailsAPI 

urlpatterns = [
    # TV Lists
    path('tv/popular', TVPopularAPI.as_view(), name='tv-popular'),

    # TV Series
    path('tv/details', TVDetailsAPI.as_view(), name='tv-details'),

    # TV Seasons
    path('tv/season/details', TVSeasonDetailsAPI.as_view(), name='tv-season-details'),
    
    # TV Episodes
    path('tv/episode/details', TVEpisodeDetailsAPI.as_view(), name='tv-episode-details'),
]
