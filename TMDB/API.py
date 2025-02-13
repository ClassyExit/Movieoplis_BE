import requests

from common_utils.variables import API_KEY


def getGenreList(language='en-US'):

    parameters = {'api_key': API_KEY, 'language': language}
    url_movie = f'https://api.themoviedb.org/3/genre/movie/list'
    url_show = f'https://api.themoviedb.org/3/genre/tv/list'

    results = {
        'movies': requests.get(url_movie, params=parameters).json(),
        'shows': requests.get(url_show, params=parameters).json()
    }

    return results





