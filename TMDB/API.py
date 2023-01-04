import requests

from common_utils.variables import API_KEY


def getMovieGenreList(language='en-US'):

    parameters = {'api_key': API_KEY, 'language': language}
    url = f'https://api.themoviedb.org/3/genre/movie/list'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getTVGenreList(language='en-US'):

    parameters = {'api_key': API_KEY, 'language': language}
    url = f'https://api.themoviedb.org/3/genre/tv/list'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results
