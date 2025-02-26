from django.urls import path

from . import views   

urlpatterns = [
    path('genres', views.GenreAPI, name='genres'),
    path('movie-videos', views.MovieVideoPlayerAPI, name='movie-videos' ),
    path('show-videos', views.ShowVideoPlayerAPI, name='show-videos'),
]
