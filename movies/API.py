import requests

from common_utils.variables import API_KEY



# Movie Lists API calls
def getPopularMovies(language='en-US', page=1):
    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = 'https://api.themoviedb.org/3/movie/popular'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getUpcomingMovies(language='en-US', page=1):
    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = 'https://api.themoviedb.org/3/movie/upcoming'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getNowPlayingMovies(language='en-US', page=1):
    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = 'https://api.themoviedb.org/3/movie/now_playing'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getMovieTopRated(language='en-US', page=1):
    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = 'https://api.themoviedb.org/3/movie/top_rated'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getMovieLatest(language='en-US'):
    parameters = {'api_key': API_KEY, 'language': language}
    url = 'https://api.themoviedb.org/3/movie/latest'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results



# Movie API calls

def getMovieDetails(movie_id, language='en-US'):
    if not movie_id:
        return 'Missing movie ID'

    parameters = {'api_key': API_KEY, 'language': language}
    url = f'https://api.themoviedb.org/3/movie/{movie_id}'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getRecommendations(movie_id, language='en-US', page=1):
    if not movie_id:
        return 'Missing movie ID'

    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getSimilarMovies(movie_id, language='en-US', page=1):
    if not movie_id:
        return 'Missing movie ID'

    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/similar'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getMovieCredits(movie_id, language='en-US'):
    if not movie_id:
        return 'Missing movie ID'

    parameters = {'api_key': API_KEY, 'language': language}
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getMovieVideos(movie_id, language='en-US'):
    parameters = {'api_key': API_KEY, 'language': language}
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getMovieProviders(movie_id):
    parameters = {'api_key': API_KEY}
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/watch/providers'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results








