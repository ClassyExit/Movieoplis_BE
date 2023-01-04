from django.shortcuts import render
from rest_framework. response import Response
from rest_framework import generics

from .API import getMovieGenreList, getTVGenreList

# Create your views here.


class TVGenreAPI(generics.RetrieveAPIView):

    def get_queryset(self):
        return getTVGenreList()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class MovieGenreAPI(generics.RetrieveAPIView):

    def get_queryset(self):
        return getMovieGenreList()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)
