from django.shortcuts import render
from rest_framework. response import Response
from rest_framework import generics

from .API import getTVDetails, getTVCredits, getTVRecommendations, getTVSimilar, getTVPopular, getTVShowsDiscover
# Create your views here.


class TVDetailsAPI(generics.RetrieveAPIView):

    def get_queryset(self):
        tv_id = self.request.query_params.get('tv_id')
        return getTVDetails(tv_id)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class TVCreditsAPI(generics.RetrieveAPIView):

    def get_queryset(self):
        tv_id = self.request.query_params.get('tv_id')
        return getTVCredits(tv_id)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class TVRecommendationsAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        tv_id = self.request.query_params.get('tv_id')
        page = self.request.query_params.get('page') or 1
        return getTVRecommendations(tv_id, page=page)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class TVSimilarAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        tv_id = self.request.query_params.get('tv_id')
        page = self.request.query_params.get('page') or 1
        return getTVSimilar(tv_id, page=page)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class TVPopularAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        page = self.request.query_params.get('page') or 1
        return getTVPopular(page=page)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class TVDiscoverAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        sort_by = self.request.query_params.get('sort_by')
        page = self.request.query_params.get('page') or 1
        vote_average = self.request.query_params.get('vote_average')
        vote_sort = self.request.query_params.get('vote_sort')
        with_genres = self.request.query_params.get('with_genres')
        with_networks = self.request.query_params.get('with_networks')

        return getTVShowsDiscover(sort_by=sort_by, page=page, vote_average=vote_average, vote_sort=vote_sort, with_genres=with_genres, with_networks=with_networks)

    def get(self, requests, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)
