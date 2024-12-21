from django.shortcuts import render
from rest_framework. response import Response
from rest_framework import generics

from .API import getCollections


class CollectionsAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        collection_id = self.request.query_params.get('collection_id')
        language = self.request.query_params.get('language') or 'en-US'

        return getCollections(collection_id=collection_id, language=language)
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)
