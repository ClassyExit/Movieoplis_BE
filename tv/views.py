from django.shortcuts import render
from rest_framework. response import Response
from rest_framework import generics

from .API_Lists import getTVPopular
from .API_Series import getTVDetails
from .API_Seasons import getTVSeasonDetails, getTVEpisodeDetails

# TV POPULAR
class TVPopularAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        page = self.request.query_params.get('page') or 1
        return getTVPopular(page=page)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)




# TV Series
class TVDetailsAPI(generics.RetrieveAPIView):

    def get_queryset(self):
        tv_id = self.request.query_params.get('tv_id')
        return getTVDetails(tv_id)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)



# TV Seasons
class TVSeasonDetailsAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        tv_id = self.request.query_params.get('tv_id')
        season_number = self.request.query_params.get('season_number')
        return getTVSeasonDetails(tv_id, season_number)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)




# TV Episodes
class TVEpisodeDetailsAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        tv_id = self.request.query_params.get('tv_id')
        season_number = self.request.query_params.get('season_number')
        episode_number = self.request.query_params.get('episode_number')
        return getTVEpisodeDetails(tv_id, season_number, episode_number)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)



