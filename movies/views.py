from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .API import getPopularMovies, getMovieDetails


# Movie Lists - Get Popular Movies
class PopularMoviesAPI(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        page = request.query_params.get('page', 1)

        try:
            page = int(page)
        except ValueError:
            return Response({'error': 'Invalid page number'}, status=status.HTTP_400_BAD_REQUEST)

        movies = getPopularMovies(page=page)
        return Response(movies, status=status.HTTP_200_OK)


# Movie Details - Get Movie by ID
class MovieDetailsAPI(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        movie_id = request.query_params.get('movie_id')

        if not movie_id:
            return Response({'error': 'movie_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            movie_details = getMovieDetails(movie_id)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(movie_details, status=status.HTTP_200_OK)
