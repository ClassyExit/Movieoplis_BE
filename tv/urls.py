from django.urls import path
from .views import TVDetailsAPI, TVCreditsAPI, TVRecommendationsAPI, TVSimilarAPI, TVPopularAPI, TVTopRatedAPI, TVVideosAPI, TVProvidersAPI, TVSeasonDetailsAPI, TVSeasonVideosAPI 

urlpatterns = [
    # TV Lists
    path('tv/popular', TVPopularAPI.as_view(), name='tv-popular'),
    path('tv/toprated', TVTopRatedAPI.as_view(), name='tv-toprated'),


    # TV Series
    path('tv/details', TVDetailsAPI.as_view(), name='tv-details'),
    path('tv/credits', TVCreditsAPI.as_view(), name='tv-credits'),
    path('tv/recommendations', TVRecommendationsAPI.as_view(),
         name='tv-recommendations'),
    path('tv/similar', TVSimilarAPI.as_view(), name='tv-similar'),
    path('tv/videos', TVVideosAPI.as_view(), name='tv-videos'),
    path('tv/providers', TVProvidersAPI.as_view(), name='tv-providers'),


    # TV Seasons
    path('tv/season/details', TVSeasonDetailsAPI.as_view(), name='tv-season-details'),
    path('tv/season/videos', TVSeasonVideosAPI.as_view(), name='tv-season-videos'),
    

    # TV Episodes

    
    
    
]
