from django.shortcuts import render
from rest_framework. response import Response
from rest_framework import generics

# Create your views here.
from .API import multiSearch


class MultiSearchAPI(generics.RetrieveAPIView):
    '''Get the reviews for a movie'''


    def format_results(results): 
        pass

    def get_queryset(self):
        query = self.request.query_params.get('query')
        page = self.request.query_params.get('page') or 1
        return multiSearch(query=query, page=page)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


