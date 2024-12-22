from django.http import HttpResponse
from django.shortcuts import render

def statuspage(request):
    return render(request, 'statuspage.html')