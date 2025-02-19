from django.urls import path

from .views import MovieDiscoverAPI, TVDiscoverAPI, TrailerDiscoverAPI


urlpatterns = [
    path('discover/movie', MovieDiscoverAPI.as_view(), name='movie-discover'),
    path('discover/tv', TVDiscoverAPI.as_view(), name='tv-discover'),
    path('discover/trailer',TrailerDiscoverAPI.as_view(), name='trailer-discover'),
]