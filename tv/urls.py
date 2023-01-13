from django.urls import path
from .views import TVDetailsAPI, TVCreditsAPI, TVRecommendationsAPI, TVSimilarAPI, TVPopularAPI, TVDiscoverAPI

urlpatterns = [
    path('tv/details', TVDetailsAPI.as_view(), name='tv-details'),
    path('tv/credits', TVCreditsAPI.as_view(), name='tv-credits'),
    path('tv/recommendations', TVRecommendationsAPI.as_view(),
         name='tv-recommendations'),
    path('tv/similar', TVSimilarAPI.as_view(), name='tv-similar'),
    path('tv/popular', TVPopularAPI.as_view(), name='tv-popular'),
    path('tv/discover', TVDiscoverAPI.as_view(), name='tv-discover')
]
