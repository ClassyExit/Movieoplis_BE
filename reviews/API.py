import requests

from common_utils.variables import API_KEY


def getMovieReviews(movie_id, page=1, language='en-US'):
    if not movie_id:
        return 'Missing movie ID'

    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/reviews'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getTVReviews(tv_id, page=1, language='en-US'):
    if not tv_id:
        return 'Missing show ID'

    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = url = f'https://api.themoviedb.org/3/tv/{tv_id}/reviews'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results
