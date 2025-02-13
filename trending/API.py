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



def getTopRated(language='en-US', page=1):
    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url_tv = 'https://api.themoviedb.org/3/tv/top_rated'
    url_movie = 'https://api.themoviedb.org/3/movie/top_rated'

    results = {

        'tv': requests.get(url_tv, params=parameters).json(),
        'movies': requests.get(url_movie, params=parameters).json()
    }

    return results