from django.shortcuts import render
from rest_framework. response import Response
from rest_framework import generics
import random

from .API import getMovieDiscover, getTVShowsDiscover, getPopularMovies, getVideos


class MovieDiscoverAPI(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        include_adult = request.query_params.get('include_adult', 'false').lower() == 'true'
        language = request.query_params.get('language', 'en-US')
        sort_by = request.query_params.get('sort_by', 'popularity.desc')
        page = int(request.query_params.get('page', 1))
        vote_average = request.query_params.get('vote_average')
        vote_sort = request.query_params.get('vote_sort')
        with_genres = request.query_params.get('with_genres')

        movies = getMovieDiscover(
            include_adult=include_adult,
            language=language,
            sort_by=sort_by,
            page=page,
            vote_average=vote_average,
            vote_sort=vote_sort,
            with_genres=with_genres
        )

        return Response(movies)


class TVDiscoverAPI(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        include_adult = request.query_params.get('include_adult', 'false').lower() == 'true'
        language = request.query_params.get('language', 'en-US')
        sort_by = request.query_params.get('sort_by', 'popularity.desc')
        page = int(request.query_params.get('page', 1))
        vote_average = request.query_params.get('vote_average')
        vote_sort = request.query_params.get('vote_sort')
        with_genres = request.query_params.get('with_genres')
        with_networks = request.query_params.get('with_networks')

        tv_shows = getTVShowsDiscover(
            include_adult=include_adult,
            language=language,
            sort_by=sort_by,
            page=page,
            vote_average=vote_average,
            vote_sort=vote_sort,
            with_genres=with_genres,
            with_networks=with_networks
        )

        return Response(tv_shows)



import random
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status

from .API import getPopularMovies, getVideos

import random
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status

from .API import getPopularMovies, getVideos

class TrailerDiscoverAPI(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        max_retries = 5  # Limit retries to prevent infinite loops
        retries = 0

        while retries < max_retries:
            page = random.randint(1, 500)  

            # Fetch popular movies
            movies = getPopularMovies(page=page)
            # print("Movies API response:", movies) 

            if not isinstance(movies, dict) or 'results' not in movies:
                return Response({'error': 'Invalid movie data received'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            if not movies['results']:
                retries += 1
                continue  # Try again

            # Select a random movie
            movie = random.choice(movies['results'])
            # print("Selected Movie:", movie)  

            # Get movie trailers
            videos = getVideos(movie['id'])
            # print("Videos API response:", videos)

            if not isinstance(videos, dict) or 'results' not in videos:
                retries += 1
                continue  # Retry if invalid video response

            # Filter for YouTube trailers
            trailers = [video for video in videos['results'] if video.get("type") == "Trailer" and video.get("site") == "YouTube"]

            if trailers:
                return Response({
                    'id': movie['id'],
                    'title': movie['title'],
                    'overview': movie['overview'],
                    'poster': movie['poster_path'],
                    'type': 'movie',
                    'trailerKey': trailers[0]['key']
                }, status=status.HTTP_200_OK)

            retries += 1

        return Response({'error': 'No trailers found after multiple attempts'}, status=status.HTTP_404_NOT_FOUND)
