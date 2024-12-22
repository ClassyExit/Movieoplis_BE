from django.shortcuts import render
from rest_framework. response import Response
from rest_framework import generics

from .API_Lists import getTVPopular, getTVTopRated
from .API_Series import getTVDetails, getTVCredits, getTVRecommendations, getTVSimilar, getTVVideos, getTVProviders 
from .API_Seasons import getTVSeasonDetails, getTVSeasonVideos, getTVEpisodeDetails

# TV LISTS
class TVPopularAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        page = self.request.query_params.get('page') or 1
        return getTVPopular(page=page)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class TVTopRatedAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        page = self.request.query_params.get('page') or 1
        return getTVTopRated(page=page)

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

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class TVVideosAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        tv_id = self.request.query_params.get('tv_id')
        return getTVVideos(tv_id)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class TVProvidersAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        tv_id = self.request.query_params.get('tv_id')
        return getTVProviders(tv_id)

    def get(self, *args, **kwargs):
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



class TVSeasonVideosAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        tv_id = self.request.query_params.get('tv_id')
        season_number = self.request.query_params.get('season_number')
        return getTVSeasonVideos(tv_id, season_number)

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



