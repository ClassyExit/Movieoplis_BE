from django.urls import path

from .views import MovieDiscoverAPI, TVDiscoverAPI


urlpatterns = [
    path('discover/movie', MovieDiscoverAPI.as_view(), name='movie-discover'),
    path('discover/tv', TVDiscoverAPI.as_view(), name='tv-discover')
]