from django.urls import path
from . import views

urlpatterns = [
    path('user', views.AddUser, name='add-user'),
    path('approve-user', views.ApproveUser, name='approve-user'),
]