from django.urls import path

from .views import TVGenreAPI, MovieGenreAPI, check_status_codes

urlpatterns = [
    path('tv/genre', TVGenreAPI.as_view(), name='genre-tv'),
    path('movie/genre', MovieGenreAPI.as_view(), name='genre-movie'),
    path('health', check_status_codes, name='status'),
    
]
