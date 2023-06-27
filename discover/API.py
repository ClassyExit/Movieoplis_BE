import requests

from common_utils.variables import API_KEY


def getMovieDiscover(language='en-US', sort_by='popularity.desc', page=1, vote_average=5, vote_sort='gte', with_genres=''):
    parameters = {'api_key': API_KEY, 'language': language,
                  'page': page, 'sort_by': sort_by, f'vote_average.{vote_sort}': vote_average, 'with_genres': with_genres}
    url = 'https://api.themoviedb.org/3/discover/movie'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getTVShowsDiscover(language='en-US', sort_by='popularity.desc', page=1, vote_average=5, vote_sort='gte', with_genres='', with_networks=''):
    parameters = {'api_key': API_KEY, 'language': language,
                  'page': page, 'sort_by': sort_by, f'vote_average.{vote_sort}': vote_average, 'with_genres': with_genres, 'with_networks': with_networks}

    url = 'https://api.themoviedb.org/3/discover/tv'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results