from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.

from common_utils.variables import API_KEY
from .API import getTrending


class TrendingAPI(generics.RetrieveAPIView):
    '''GET THE TRENDIND CONTENT FOR THE DAY'''

    def get_queryset(self):
        media_type = self.request.query_params.get('media_type')
        time_window = self.request.query_params.get('time_window')

        return getTrending(media_type, time_window)

    def get(self, request, *args, **kawrgs):
        queryset = self.get_queryset()

        return Response(queryset)
