import requests


from common_utils.variables import API_KEY


def multiSearch(query, language='en-US', page=1):
    if not query:
        return 'Missing query search'

    parameters = {'api_key': API_KEY,
                  'language': language, 'query': query, 'page': page}
    url1 = f'https://api.themoviedb.org/3/search/tv'

    url2 = f'https://api.themoviedb.org/3/search/movie'

    res1 = requests.get(url1, params=parameters)
    res2 = requests.get(url2, params=parameters)

    results = {
        'tv': res1.json(),
        'movies': res2.json()
    }

    return results

