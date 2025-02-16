from django.shortcuts import render
from rest_framework import status
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ListItem
from common_utils.get_uid_from_request import get_uid_from_request


@api_view(['GET', 'POST', 'DELETE'])
def ListAPI(request): 
    # Pass uid from Firebase to get specific user's list
    if request.method == 'GET':
        # GET USER'S LIST
        firebase_uid, error_response = get_uid_from_request(request)

        if error_response:
            return error_response
        
        list_items = ListItem.objects.filter(firebase_uid=firebase_uid)

        list_data = [
                {
                    'title': item.title,
                    'overview': item.overview,
                    'poster': item.poster,
                    'type': item.type,
                    'created_at': item.created_at
                }
                for item in list_items
            ]
        
        response_data = {
            'results': list_data,
            'status':status.HTTP_200_OK
        }

        return Response(response_data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        # ADD ITEM TO LIST
        firebase_uid, error_response = get_uid_from_request(request)

        if error_response:
            return error_response
        
        # Get data from request
        title = request.data.get('title')
        overview = request.data.get('overview')
        poster = request.data.get('poster')
        item_type = request.data.get('type')  # Avoid using 'type' directly as it can conflict with Python's built-in type()

        # Create a new ListItem instance
        new_item = ListItem.objects.create(
            firebase_uid=firebase_uid,
            title=title,
            overview=overview,
            poster=poster,
            type=item_type
        )

        # Save the new item
<<<<<<< HEAD
        new_item.save()
=======
        new_item.save(using='default')
>>>>>>> 0a021405f5a2abcb9e07e28d34b160761e3d5f28

        return Response({'success': 'Item added successfully'}, status=status.HTTP_201_CREATED)


    elif request.method == 'DELETE':
        # DELETE ITEM FROM LIST

        firebase_uid, error_response = get_uid_from_request(request)

        if error_response:
            return error_response
        
        # Delete item from list by item_id
        delete_item_id = request.data.get('item_id')

        # Check if item_id is provided
        if not delete_item_id:
            return Response({'error': 'Item ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Get the item to delete
        item_to_delete = ListItem.objects.filter(firebase_uid=firebase_uid, item_id=delete_item_id)

        if not item_to_delete:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
<<<<<<< HEAD
            item_to_delete.delete()
=======
            item_to_delete.delete(using='default')
>>>>>>> 0a021405f5a2abcb9e07e28d34b160761e3d5f28
        return Response({'success': 'Item deleted successfully'}, status=status.HTTP_201_CREATED)