from django.shortcuts import render
from rest_framework. response import Response
from rest_framework import generics

# Create your views here.

from .API import getMovieReviews, getTVReviews


class MovieReviewAPI(generics.RetrieveAPIView):
    '''Get the reviews for a movie'''

    def get_queryset(self):
        movie_id = self.request.query_params.get('movie_id')
        page = self.request.query_params.get('page')

        return getMovieReviews(movie_id, page=page)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        return Response(queryset)


class TVReviewAPI(generics.RetrieveAPIView):
    '''Get the reviews for TV shows'''

    def get_queryset(self):
        tv_id = self.request.query_params.get('tv_id')
        page = self.request.query_params.get('page')

        return getTVReviews(tv_id, page=page)

    def get(self, requests, *args, **kwargs):
        queryset = self.get_queryset()

        return Response(queryset)
