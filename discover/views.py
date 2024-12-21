from django.shortcuts import render
from rest_framework. response import Response
from rest_framework import generics

from .API import getMovieDiscover, getTVShowsDiscover


class MovieDiscoverAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        include_adult = self.request.query_params.get('include_adult') or False
        language = self.request.query_params.get('language') or 'en-US'
        sort_by = self.request.query_params.get('sort_by')
        page = self.request.query_params.get('page')
        vote_average = self.request.query_params.get('vote_average')
        vote_sort = self.request.query_params.get('vote_sort')
        with_genres = self.request.query_params.get('with_genres')

        return getMovieDiscover(include_adult=include_adult, language=language, sort_by=sort_by, page=page, vote_average=vote_average, vote_sort=vote_sort, with_genres=with_genres)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)



class TVDiscoverAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        include_adult = self.request.query_params.get('include_adult') or False
        language = self.request.query_params.get('language') or 'en-US'
        sort_by = self.request.query_params.get('sort_by')
        page = self.request.query_params.get('page') or 1
        vote_average = self.request.query_params.get('vote_average')
        vote_sort = self.request.query_params.get('vote_sort')
        with_genres = self.request.query_params.get('with_genres')
        with_networks = self.request.query_params.get('with_networks')

        return getTVShowsDiscover(include_adult=include_adult, language=language, sort_by=sort_by, page=page, vote_average=vote_average, vote_sort=vote_sort, with_genres=with_genres, with_networks=with_networks)

    def get(self, requests, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)