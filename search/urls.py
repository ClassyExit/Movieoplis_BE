from django.urls import path
from .views import  MultiSearchAPI
from . import views


urlpatterns = [
    path('search', MultiSearchAPI.as_view(), name='search-multi'),
    path("song/search", views.search_songs, name="search_songs"),
]
