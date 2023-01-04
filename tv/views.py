from django.shortcuts import render
from rest_framework. response import Response
from rest_framework import generics

from .API import getTVDetails, getTVCredits, getTVRecommendations, getTVSimilar, getTVPopular
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
