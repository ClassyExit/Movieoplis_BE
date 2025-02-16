import requests

from common_utils.variables import API_KEY


def getTVPopular(language='en-US', page=1):
    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = f'https://api.themoviedb.org/3/tv/popular'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results
