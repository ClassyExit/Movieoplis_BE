from django.urls import path
from . import views


#TODO: Add url to main url file (uncomment it)
urlpatterns = [
    path('list', views.ListAPI, name='list'),
]