import requests

from common_utils.variables import API_KEY


def getTVSeasonDetails(tv_id, season_number):

    parameters = {'api_key': API_KEY}
    url = f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getTVSeasonVideos(tv_id, season_number):
    parameters = {'api_key': API_KEY}
    url = f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/videos'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results