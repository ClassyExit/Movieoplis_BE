import requests

from common_utils.variables import API_KEY


def getTVDetails(tv_id, language='en-US'):
    if not tv_id:
        return 'Missing movie ID'

    parameters = {'api_key': API_KEY, 'language': language}
    url = f'https://api.themoviedb.org/3/tv/{tv_id}'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getTVCredits(tv_id, language='en-US'):
    if not tv_id:
        return 'Missing movie ID'

    parameters = {'api_key': API_KEY, 'language': language}
    url = f'https://api.themoviedb.org/3/tv/{tv_id}/credits'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getTVRecommendations(tv_id, language='en-US', page=1):
    if not tv_id:
        return 'Missing movie ID'

    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = f'https://api.themoviedb.org/3/tv/{tv_id}/recommendations'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getTVSimilar(tv_id, language='en-US', page=1):
    if not tv_id:
        return 'Missing movie ID'

    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = f'https://api.themoviedb.org/3/tv/{tv_id}/similar'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getTVPopular(language='en-US', page=1):
    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = f'https://api.themoviedb.org/3/tv/popular'

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
