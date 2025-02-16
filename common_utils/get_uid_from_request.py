from rest_framework import status
from rest_framework.response import Response

def get_uid_from_request(request):
    """
    Extracts the UID from the request headers.
    """
    # Get the uid from the headers
    firebase_uid = request.headers.get('uid')
    
    # Validate the uid
    if not firebase_uid:
        return None, Response({'error': 'UID header is missing'}, status=status.HTTP_400_BAD_REQUEST)
    
    return firebase_uid, None
