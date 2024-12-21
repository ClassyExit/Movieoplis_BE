from django.urls import path

from .views import CollectionsAPI

urlpatterns = [
    path('collections', CollectionsAPI.as_view(), name='collections')
]