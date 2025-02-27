from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view
import requests

from common_utils.get_uid_from_request import get_uid_from_request
from .API import getGenreList, getMovieVideosLinks, getShowVideoLinks


# Genres API
@api_view(['GET'])
def GenreAPI(request):
    results = getGenreList()
    return Response(results)


# Movie Video Player API
@api_view(['GET'])
def MovieVideoPlayerAPI(request):
    # Get movie_id from query parameters
    movie_id = request.query_params.get('movie_id')
    if not movie_id:
        return Response({'error': 'movie_id is required'}, status=status.HTTP_400_BAD_REQUEST)

    results = getMovieVideosLinks(movie_id)

    return Response({'results': results}, status=status.HTTP_200_OK)


# Show Video Player API
@api_view(['GET'])
def ShowVideoPlayerAPI(request):
    # Get TV show details from query parameters
    tv_id = request.query_params.get('tv_id')
    season_number = request.query_params.get('season_number')
    episode_number = request.query_params.get('episode_number')

    if not tv_id or not season_number or not episode_number:
        return Response({'error': 'tv_id, season_number, and episode_number are required'},
                        status=status.HTTP_400_BAD_REQUEST)

    results = getShowVideoLinks(tv_id=tv_id, season_number=season_number, episode_number=episode_number)

    return Response({'results': results}, status=status.HTTP_200_OK)
