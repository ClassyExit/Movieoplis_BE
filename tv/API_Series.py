import requests

from common_utils.variables import API_KEY


def getTVDetails(tv_id, language='en-US', page=1):
    if not tv_id:
        return 'Missing movie ID'

    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url_details = f'https://api.themoviedb.org/3/tv/{tv_id}'
    url_credits = f'https://api.themoviedb.org/3/tv/{tv_id}/credits'
    url_recommendations = f'https://api.themoviedb.org/3/tv/{tv_id}/recommendations'
    url_similar = f'https://api.themoviedb.org/3/tv/{tv_id}/similar'
    url_videos = f'https://api.themoviedb.org/3/tv/{tv_id}/videos'
    url_providers = f'https://api.themoviedb.org/3/tv/{tv_id}/watch/providers'

    results = {
        'details': requests.get(url_details, params=parameters).json(),
        'credits': requests.get(url_credits, params=parameters).json(),
        'recommendations': requests.get(url_recommendations, params=parameters).json(),
        'similar': requests.get(url_similar, params=parameters).json(),
        'videos': requests.get(url_videos, params=parameters).json(),
        'providers': requests.get(url_providers, params=parameters).json()
    }

    return results











