import requests

from common_utils.variables import API_KEY


def getCollections(collection_id, language='en-US', ):
    """Returns all movies in a collection based on the collection_id"""
    if not collection_id: 
        return 
    
    parameters = {'api_key': API_KEY, 'language': language}

    url = f'https://api.themoviedb.org/3/collection/{collection_id}'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results
    