import requests


from common_utils.variables import API_KEY


def multiSearch(query, language='en-US', page=1):
    if not query:
        return 'Missing query search'

    parameters = {'api_key': API_KEY,
                  'language': language, 'query': query, 'page': page}
    url_tv = f'https://api.themoviedb.org/3/search/tv'
    url_movie = f'https://api.themoviedb.org/3/search/movie'

    results = {
        'tv': requests.get(url_tv, params=parameters).json(),
        'movies': requests.get(url_movie, params=parameters).json()
    }

    return results

