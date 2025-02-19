from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status

# Import API functions
from .API import getMovieReviews, getTVReviews


class MovieReviewAPI(generics.ListAPIView):
    '''Get the reviews for a movie'''

    def get(self, request, *args, **kwargs):
        movie_id = request.query_params.get('movie_id')
        page = request.query_params.get('page', 1)

        if not movie_id:
            return Response({'error': 'movie_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            page = int(page)
        except ValueError:
            return Response({'error': 'Invalid page number'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            reviews = getMovieReviews(movie_id, page=page)
            return Response(reviews, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TVReviewAPI(generics.ListAPIView):
    '''Get the reviews for a TV show'''

    def get(self, request, *args, **kwargs):
        tv_id = request.query_params.get('tv_id')
        page = request.query_params.get('page', 1)

        if not tv_id:
            return Response({'error': 'tv_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            page = int(page)
        except ValueError:
            return Response({'error': 'Invalid page number'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            reviews = getTVReviews(tv_id, page=page)
            return Response(reviews, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
