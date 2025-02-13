from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET', 'POST', 'DELETE'])
def ListAPI(request): 

    if request.method == 'GET':
        # GET LIST TO USER
        return Response('GET')

    elif request.method == 'POST':
        # ADD ITEM TO LIST
        return Response('POST')

    elif request.method == 'DELETE':
        # DELETE ITEM FROM LIST
        return Response('DELETE')