from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ListItem
from common_utils.get_uid_from_request import get_uid_from_request


@api_view(['GET', 'POST', 'DELETE'])
def ListAPI(request): 
    # Get the Firebase UID from request
    firebase_uid, error_response = get_uid_from_request(request)
    if error_response:
        return error_response

    if request.method == 'GET':
        # GET USER'S LIST
        list_items = ListItem.objects.filter(firebase_uid=firebase_uid)

        list_data = [
            {   
                'item_id': item.item_id,
                'title': item.title,
                'overview': item.overview,
                'poster': item.poster,
                'type': item.type,
                'created_at': item.created_at
            }
            for item in list_items
        ]
        
        return Response({'results': list_data}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        # ADD ITEM TO LIST
        required_fields = ['item_id', 'title', 'overview', 'poster', 'type']
        for field in required_fields:
            if field not in request.data:
                return Response({'error': f'{field} is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Extract data
        item_id = request.data.get('item_id')
        title = request.data.get('title')
        overview = request.data.get('overview')
        poster = request.data.get('poster')
        item_type = request.data.get('type') 

        # Check if the item already exists
        if ListItem.objects.filter(firebase_uid=firebase_uid, item_id=item_id).exists():
            return Response({'error': 'Item already exists in the list'}, status=status.HTTP_400_BAD_REQUEST)

        # Create and save the item
        new_item = ListItem.objects.create(
            item_id=item_id,
            firebase_uid=firebase_uid,
            title=title,
            overview=overview,
            poster=poster,
            type=item_type
        )
        new_item.save()

        return Response({'success': 'Item added successfully'}, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        # DELETE ITEM FROM LIST
        delete_item_id = request.data.get('item_id')

        if not delete_item_id:
            return Response({'error': 'Item ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Get the item and delete if exists
        item_to_delete = ListItem.objects.filter(firebase_uid=firebase_uid, item_id=delete_item_id)

        if not item_to_delete.exists():
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        item_to_delete.delete()
        return Response({'success': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
