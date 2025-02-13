from django.shortcuts import render
from rest_framework. response import Response
from rest_framework import generics

from .API import   getPopularMovies, getMovieDetails




# Movie Lists
class PopularMoviesAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        page = self.request.query_params.get('page') or 1
        return getPopularMovies(page=page)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


# Movies
class MovieDetailsAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        movie_id = self.request.query_params.get('movie_id')
        return getMovieDetails(movie_id)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset() 
        return Response(queryset)
    

















