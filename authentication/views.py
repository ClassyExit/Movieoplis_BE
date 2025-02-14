from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from common_utils.get_uid_from_request import get_uid_from_request



@api_view(['POST', 'DELETE'])
def AddUser(request):
    if request.method == 'POST':
        # ADD USER TO MATCH FIREBASE UID
        firebase_uid, error_response = get_uid_from_request(request)

        if error_response:
            return error_response
        
        data = {
            'firebase_uid': firebase_uid
        }

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save(using='default')
            return Response({'success': 'Item added successfully'}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # DELETE USER
        firebase_uid, error_response = get_uid_from_request(request)

        if error_response:
            return error_response

        
        try: 
            # Check if user exists
            delete_user = User.objects.get(firebase_uid=firebase_uid)
            delete_user.delete(using='default')
            return Response({'success': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        
            
        