'''API Call for trending'''
import requests

from common_utils.variables import API_KEY


def getTrending(media_type='all', time_window='week'):
    '''Get Trending movie content'''
    parameters = {'api_key': API_KEY, }
    url = f'https://api.themoviedb.org/3/trending/{media_type}/{time_window}'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results
