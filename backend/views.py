from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render

def statuspage(request):
    return render(request, 'status.html')


