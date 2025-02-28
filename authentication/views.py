from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, UserVideoPermissionQueue
from .serializers import UserSerializer
from common_utils.get_uid_from_request import get_uid_from_request


@api_view(['POST', 'DELETE', 'GET'])
def AddUser(request):
    if request.method == 'POST':
        # ADD USER TO MATCH FIREBASE UID
        firebase_uid, error_response = get_uid_from_request(request)
        if error_response:
            return error_response
        
        data = {'firebase_uid': firebase_uid}
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Item added successfully'}, status=status.HTTP_201_CREATED)
        
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # DELETE USER
        firebase_uid, error_response = get_uid_from_request(request)
        if error_response:
            return error_response

        try:
            # Check if user exists
            delete_user = User.objects.filter(firebase_uid=firebase_uid)  
            if not delete_user.exists():
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            delete_user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'GET':
        # GET USER INFO
        firebase_uid, error_response = get_uid_from_request(request)
        if error_response:
            return error_response
        
        user_info = User.objects.filter(firebase_uid=firebase_uid).first()

        if not user_info:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'id': user_info.firebase_uid, 'canViewVideos': user_info.canViewVideos, 'isAdmin': user_info.isAdmin}, status=status.HTTP_200_OK)
        


@api_view(['POST', 'GET'])
def ApproveUser(request):

    if request.method == 'GET':
        # GET USER INFO
        firebase_uid, error_response = get_uid_from_request(request)
        if error_response:
            return error_response
        
        # Check if user is admin
        user_info = User.objects.filter(firebase_uid=firebase_uid).first()

        if user_info is not user_info.isAdmin:
            return Response({'Authorization': 'Invalid permissions'}, status=status.HTTP_404_NOT_FOUND)

        # Return queue
        queue = UserVideoPermissionQueue.objects.all()

        if not queue:
            return Response({'error': 'No items in queue'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'queue': queue}, status=status.HTTP_200_OK)        
          

    elif request.method == 'POST':
        """
        Approves a user by updating their canViewVideos field to True
        """
        firebase_uid, error_response = get_uid_from_request(request)
        if error_response:
            return error_response
        
        try:
            # Check if the user exists in the queue
            queue_entry = UserVideoPermissionQueue.objects.filter(firebase_uid=firebase_uid).first()
            if not queue_entry:
                return Response({'error': 'User not found in the permission queue'}, status=status.HTTP_404_NOT_FOUND)
            
            # Check if the user exists in the User model
            user = User.objects.filter(firebase_uid=firebase_uid).first()
            if not user:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            
            # Approve the user
            user.canViewVideos = True
            user.save()
            
            # Remove the user from the queue
            queue_entry.delete()
            
            return Response({'success': 'User approved successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)