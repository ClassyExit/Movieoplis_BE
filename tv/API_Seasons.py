import requests

from common_utils.variables import API_KEY


def getTVSeasonDetails(tv_id, season_number):

    parameters = {'api_key': API_KEY}
    url_details = f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}'
    url_videos = f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/videos'

    results = {
        'details': requests.get(url_details, params=parameters).json(),
        'videos': requests.get(url_videos, params=parameters).json()
    }

    return results



def getTVEpisodeDetails(tv_id, season_number, episode_number):
    parameters = {'api_key': API_KEY}

    url = f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results