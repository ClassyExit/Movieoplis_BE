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



def getTVVideos(tv_id, language='en-US'):
    parameters = {'api_key': API_KEY, 'language': language}
    url = f'https://api.themoviedb.org/3/tv/{tv_id}/videos'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getTVProviders(tv_id):
    parameters = {'api_key': API_KEY}
    url = f'https://api.themoviedb.org/3/tv/{tv_id}/watch/providers'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results







