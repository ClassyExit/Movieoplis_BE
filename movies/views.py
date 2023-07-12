from django.shortcuts import render
from rest_framework. response import Response
from rest_framework import generics

from .API import getMovieCredits, getRecommendations, getSimilarMovies, getPopularMovies, getUpcomingMovies, getMovieDetails, getMovieLatest, getMovieTopRated, getNowPlayingMovies, getMovieVideos, getMovieProviders




# Movie Lists
class PopularMoviesAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        page = self.request.query_params.get('page') or 1
        return getPopularMovies(page=page)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class UpcomingMoviesAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        page = self.request.query_params.get('page') or 1
        return getUpcomingMovies(page=page)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class MovieTopRatedAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        page = self.request.query_params.get('page') or 1
        return getMovieTopRated(page=page)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class NowPlayingMoviesAPI(generics.RetrieveAPIView):
    def get_queryset(self):
         page = self.request.query_params.get('page') or 1
         return getNowPlayingMovies(page=page)
    
    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)
    

class MovieLatestAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        return getMovieLatest()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)



# Movies
class MovieDetailsAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        movie_id = self.request.query_params.get('movie_id')
        return getMovieDetails(movie_id)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)
    


class MovieRecommendationsAPI(generics.RetrieveAPIView):
    '''Get the reviews for a movie'''

    def get_queryset(self):
        movie_id = self.request.query_params.get('movie_id')
        page = self.request.query_params.get('page') or 1
        return getRecommendations(movie_id, page=page)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class SimilarMoviesAPI(generics.RetrieveAPIView):

    def get_queryset(self):
        movie_id = self.request.query_params.get('movie_id')
        page = self.request.query_params.get('page') or 1
        return getSimilarMovies(movie_id, page=page)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class MovieCreditsAPI(generics.RetrieveAPIView):
    '''Get the reviews for a movie'''

    def get_queryset(self):
        movie_id = self.request.query_params.get('movie_id')
        return getMovieCredits(movie_id)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class MovieVideosAPI(generics.RetrieveAPIView):
    '''Get the videos associated with the movie'''

    def get_queryset(self):
        movie_id = self.request.query_params.get('movie_id')
        return getMovieVideos(movie_id=movie_id)
    
    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)



class MovieProvidersAPI(generics.RetrieveAPIView):
    '''Get the videos associated with the movie'''

    def get_queryset(self):
        movie_id = self.request.query_params.get('movie_id')
        return getMovieProviders(movie_id=movie_id)
    
    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        # Return only US providers
        return Response(queryset['results']['US'])





