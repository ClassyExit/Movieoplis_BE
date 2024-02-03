from django.shortcuts import render
from rest_framework. response import Response
from rest_framework import generics

# Create your views here.
from .API import searchMovie, searchTV, multiSearch, getCollections


class MovieSearchAPI(generics.RetrieveAPIView):
    '''Get the reviews for a movie'''

    def get_queryset(self):
        query = self.request.query_params.get('query')
        page = self.request.query_params.get('page') or 1
        return searchMovie(query=query, page=page)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class TVSearchAPI(generics.RetrieveAPIView):
    '''Get the reviews for a movie'''

    def get_queryset(self):
        query = self.request.query_params.get('query')
        page = self.request.query_params.get('page') or 1
        return searchTV(query=query, page=page)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class MultiSearchAPI(generics.RetrieveAPIView):
    '''Get the reviews for a movie'''

    def get_queryset(self):
        query = self.request.query_params.get('query')
        page = self.request.query_params.get('page') or 1
        return multiSearch(query=query, page=page)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)



class getCollectionsAPI(generics.RetrieveAPIView):
    '''Get the collections for a given id'''

    def get_queryset(self):
       id = self.request.query_params.get('id')
       return getCollections(collection_id =id )
    
    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)