from django.urls import path
from .views import MovieSearchAPI, TVSearchAPI, MultiSearchAPI


urlpatterns = [
    path('search/movie', MovieSearchAPI.as_view(), name='search-movie'),
    path('search/tv', TVSearchAPI.as_view(), name='search-tv'),
    path('search/multi', MultiSearchAPI.as_view(), name='search-multi'),

]
