from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, UserVideoPermissionQueue
from .serializers import UserSerializer, QueueSerializer
from common_utils.get_uid_from_request import get_uid_from_request


@api_view(['POST', 'DELETE', 'GET', 'PATCH'])
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
            return Response({'success': 'User added successfully'}, status=status.HTTP_201_CREATED)

        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # DELETE USER
        firebase_uid, error_response = get_uid_from_request(request)
        if error_response:
            return error_response

        try:
            delete_user = User.objects.filter(firebase_uid=firebase_uid)
            if not delete_user.exists():
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            delete_user.delete()
            return Response({'success': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'GET':
        # GET USER INFO
        firebase_uid, error_response = get_uid_from_request(request)
        if error_response:
            return error_response

        user_info = User.objects.filter(firebase_uid=firebase_uid).first()

        ticket_info = UserVideoPermissionQueue.objects.filter(firebase_uid=firebase_uid).first()

        ticket_info_data = ''
        if ticket_info:
            ticket_info_data = 'In review'
        

        if not user_info:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            {'id': user_info.firebase_uid, 'canViewVideos': user_info.canViewVideos, 'isAdmin': user_info.isAdmin, 'ticket_info_data': ticket_info_data},
            status=status.HTTP_200_OK
        )

    elif request.method == 'PATCH':
        # UPDATE USER PERMISSIONS
        firebase_uid, error_response = get_uid_from_request(request)
        if error_response:
            return error_response

        user_info = User.objects.filter(firebase_uid=firebase_uid).first()
        if not user_info:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if not user_info.isAdmin:
            return Response({'error': 'Invalid permissions'}, status=status.HTTP_403_FORBIDDEN)

        user_update_uid = request.data.get('update_uid')
        if not user_update_uid:
            return Response({'error': 'No user ID provided'}, status=status.HTTP_400_BAD_REQUEST)

        update_user_info = User.objects.filter(firebase_uid=user_update_uid).first()
        if not update_user_info:
            return Response({'error': 'User to update does not exist'}, status=status.HTTP_404_NOT_FOUND)

        update_user_info.canViewVideos = True
        update_user_info.save()

        # Remove the user from the queue
        UserVideoPermissionQueue.objects.filter(firebase_uid=user_update_uid).delete()

        return Response({'success': 'User approved successfully'}, status=status.HTTP_200_OK)


@api_view(['POST', 'GET', 'DELETE'])
def ApproveUser(request):
    if request.method == 'GET':
        # GET QUEUE FOR ADMIN USERS
        firebase_uid, error_response = get_uid_from_request(request)
        if error_response:
            return error_response

        user_info = User.objects.filter(firebase_uid=firebase_uid).first()
        if not user_info:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if not user_info.isAdmin:
            return Response({'error': 'Invalid permissions'}, status=status.HTTP_403_FORBIDDEN)

        queue = UserVideoPermissionQueue.objects.all()
        if not queue.exists():
            return Response({'error': 'No items in queue'}, status=status.HTTP_404_NOT_FOUND)

        queue_data = [{'firebase_uid': item.firebase_uid} for item in queue]
        return Response({'queue': queue_data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # USERS SUBMIT TICKET TO BE APPROVED
        firebase_uid, error_response = get_uid_from_request(request)
        if error_response:
            return error_response

        try:
            data = {'firebase_uid': firebase_uid}
            serializer = QueueSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'Ticket added successfully'}, status=status.HTTP_201_CREATED)

            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'DELETE':
        # REMOVE TICKET FOR DECLINED USERS
        firebase_uid, error_response = get_uid_from_request(request)
        if error_response:
            return error_response

        user_update_uid = request.data.get('update_uid')
        if not user_update_uid:
            return Response({'error': 'No user ID provided'}, status=status.HTTP_400_BAD_REQUEST)

        queue_entry = UserVideoPermissionQueue.objects.filter(firebase_uid=user_update_uid).first()
        if queue_entry:
            queue_entry.delete()
            return Response({'success': 'Ticket deleted successfully'}, status=status.HTTP_200_OK)

        return Response({'error': 'No ticket found'}, status=status.HTTP_404_NOT_FOUND)
