from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
import requests

from .API import getMovieGenreList, getTVGenreList

# Create your views here.


class TVGenreAPI(generics.RetrieveAPIView):

    def get_queryset(self):
        return getTVGenreList()

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class MovieGenreAPI(generics.RetrieveAPIView):

    def get_queryset(self):
        return getMovieGenreList()

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)



# @api_view(['GET'])
# def check_status_codes(request):
#     endpoints = [
#     {'name': 'api/collections', 'url': 'https://tmdb-backend.herokuapp.com/api/collections', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/collections'},
#     {'name': 'api/discover/movie', 'url': 'https://tmdb-backend.herokuapp.com/api/discover/movie', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/discover/movie'},
#     {'name': 'api/discover/tv', 'url': 'https://tmdb-backend.herokuapp.com/api/discover/tv', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/discover/tv'},
#     {'name': 'api/tv/genre', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/genre', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/genre'},
#     {'name': 'api/movie/genre', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/genre', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/genre'},
#     {'name': 'api/movie/popular', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/popular', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/popular'},
#     {'name': 'api/movie/upcoming', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/upcoming', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/upcoming'},
#     {'name': 'api/movie/toprated', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/toprated', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/toprated'},
#     {'name': 'api/movie/nowplaying', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/nowplaying', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/nowplaying'},
#     {'name': 'api/movie/details', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/details', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/details'},
#     {'name': 'api/movie/recommendations', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/recommendations', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/recommendations'},
#     {'name': 'api/movie/similar', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/similar', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/similar'},
#     {'name': 'api/movie/credits', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/credits', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/credits'},
#     {'name': 'api/movie/videos', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/videos', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/videos'},
#     {'name': 'api/movie/providers', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/providers', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/providers'},
#     {'name': 'api/movie/review', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/review', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/review'},
#     {'name': 'api/tv/review', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/review', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/review'},
#     {'name': 'api/search/movie', 'url': 'https://tmdb-backend.herokuapp.com/api/search/movie', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/search/movie'},
#     {'name': 'api/search/tv', 'url': 'https://tmdb-backend.herokuapp.com/api/search/tv', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/search/tv'},
#     {'name': 'api/search/multi', 'url': 'https://tmdb-backend.herokuapp.com/api/search/multi', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/search/multi'},
#     {'name': 'api/search/collections', 'url': 'https://tmdb-backend.herokuapp.com/api/search/collections', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/search/collections'},
#     {'name': 'api/tv/popular', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/popular', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/popular'},
#     {'name': 'api/tv/toprated', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/toprated', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/toprated'},
#     {'name': 'api/tv/details', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/details', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/details'},
#     {'name': 'api/tv/credits', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/credits', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/credits'},
#     {'name': 'api/tv/recommendations', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/recommendations', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/recommendations'},
#     {'name': 'api/tv/similar', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/similar', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/similar'},
#     {'name': 'api/tv/videos', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/videos', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/videos'},
#     {'name': 'api/tv/providers', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/providers', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/providers'},
#     {'name': 'api/tv/season/details', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/season/details', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/season/details'},
#     {'name': 'api/tv/season/videos', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/season/videos', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/season/videos'},
#     {'name': 'api/tv/episode/details', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/episode/details', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/episode/details'},
#     {'name': 'api/trending', 'url': 'https://tmdb-backend.herokuapp.com/api/trending', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/trending'}
# ]
    
#     if request.method == 'GET':
        
#         status_codes = []
#         for endpoint in endpoints:
#             try:
#                 # Send a GET request to each endpoint
#                 response = requests.get(endpoint['url'])
#                 status_codes.append({
#                     'name': endpoint['name'],
#                     'status_code': response.status_code
#                 })
#             except requests.RequestException as e:
#                 status_codes.append({
#                     'name': endpoint['name'],
#                     'status_code': 'Error', 
#                     'message': str(e)
#                 })
#             else: 
#                 # Follow up on the sleeping URL
#                 response = requests.get(endpoint['sleeping_url'])
#                 status_codes.append({
#                     'name': endpoint['name'],
#                     'status_code': response.status_code
#                 })

#     return Response(status_codes)
        


class StatusPageAPI(generics.RetrieveAPIView):

    def get_queryset(self):
        endpoints = [
    {'name': 'api/collections', 'url': 'https://tmdb-backend.herokuapp.com/api/collections', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/collections'},
    {'name': 'api/discover/movie', 'url': 'https://tmdb-backend.herokuapp.com/api/discover/movie', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/discover/movie'},
    {'name': 'api/discover/tv', 'url': 'https://tmdb-backend.herokuapp.com/api/discover/tv', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/discover/tv'},
    {'name': 'api/tv/genre', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/genre', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/genre'},
    {'name': 'api/movie/genre', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/genre', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/genre'},
    {'name': 'api/movie/popular', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/popular', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/popular'},
    {'name': 'api/movie/upcoming', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/upcoming', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/upcoming'},
    {'name': 'api/movie/toprated', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/toprated', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/toprated'},
    {'name': 'api/movie/nowplaying', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/nowplaying', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/nowplaying'},
    {'name': 'api/movie/details', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/details', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/details'},
    {'name': 'api/movie/recommendations', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/recommendations', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/recommendations'},
    {'name': 'api/movie/similar', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/similar', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/similar'},
    {'name': 'api/movie/credits', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/credits', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/credits'},
    {'name': 'api/movie/videos', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/videos', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/videos'},
    {'name': 'api/movie/providers', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/providers', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/providers'},
    {'name': 'api/movie/review', 'url': 'https://tmdb-backend.herokuapp.com/api/movie/review', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/movie/review'},
    {'name': 'api/tv/review', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/review', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/review'},
    {'name': 'api/search/movie', 'url': 'https://tmdb-backend.herokuapp.com/api/search/movie', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/search/movie'},
    {'name': 'api/search/tv', 'url': 'https://tmdb-backend.herokuapp.com/api/search/tv', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/search/tv'},
    {'name': 'api/search/multi', 'url': 'https://tmdb-backend.herokuapp.com/api/search/multi', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/search/multi'},
    {'name': 'api/search/collections', 'url': 'https://tmdb-backend.herokuapp.com/api/search/collections', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/search/collections'},
    {'name': 'api/tv/popular', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/popular', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/popular'},
    {'name': 'api/tv/toprated', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/toprated', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/toprated'},
    {'name': 'api/tv/details', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/details', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/details'},
    {'name': 'api/tv/credits', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/credits', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/credits'},
    {'name': 'api/tv/recommendations', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/recommendations', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/recommendations'},
    {'name': 'api/tv/similar', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/similar', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/similar'},
    {'name': 'api/tv/videos', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/videos', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/videos'},
    {'name': 'api/tv/providers', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/providers', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/providers'},
    {'name': 'api/tv/season/details', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/season/details', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/season/details'},
    {'name': 'api/tv/season/videos', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/season/videos', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/season/videos'},
    {'name': 'api/tv/episode/details', 'url': 'https://tmdb-backend.herokuapp.com/api/tv/episode/details', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/tv/episode/details'},
    {'name': 'api/trending', 'url': 'https://tmdb-backend.herokuapp.com/api/trending', 'sleeping_url': 'https://tmdb-backend.autoidleapp.com/api/trending'}
]
    
        status_codes = []
        for endpoint in endpoints:
            try:
                # Send a GET request to each endpoint
                response = requests.get(endpoint['url'])
                status_codes.append({
                    'name': endpoint['name'],
                    'status_code': response.status_code,
                    'message': 'Success'
                })
            except requests.RequestException as e:
                status_codes.append({
                    'name': endpoint['name'],
                    'status_code': 'Error', 
                    'message': str(e)
                })
            else: 
                # Follow up on the sleeping URL
                response = requests.get(endpoint['sleeping_url'])
                status_codes.append({
                    'name': endpoint['name'],
                    'status_code': response.status_code
                })
            
        return status_codes    
    
    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)

        