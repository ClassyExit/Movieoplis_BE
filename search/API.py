import requests


from common_utils.variables import API_KEY


def searchMovie(query, language='en-US', page=1):
    if not query:
        return 'Missing query search'

    parameters = {'api_key': API_KEY,
                  'language': language, 'query': query, 'page': page}
    url = f'https://api.themoviedb.org/3/search/movie'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def searchTV(query, language='en-US', page=1):
    if not query:
        return 'Missing query search'

    parameters = {'api_key': API_KEY,
                  'language': language, 'query': query, 'page': page}
    url = f'https://api.themoviedb.org/3/search/tv'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def multiSearch(query, language='en-US', page=1):
    if not query:
        return 'Missing query search'

    parameters = {'api_key': API_KEY,
                  'language': language, 'query': query, 'page': page}
    url = f'https://api.themoviedb.org/3/search/multi'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results
