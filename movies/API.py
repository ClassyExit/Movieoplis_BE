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



# Movie API calls

def getMovieDetails(movie_id, language='en-US'):
    if not movie_id:
        return 'Missing movie ID'

    parameters = {'api_key': API_KEY, 'language': language}
    url_details = f'https://api.themoviedb.org/3/movie/{movie_id}'
    url_recommendations = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
    url_similar = f'https://api.themoviedb.org/3/movie/{movie_id}/similar'
    url_credits = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
    url_videos = f'https://api.themoviedb.org/3/movie/{movie_id}/videos'
    url_provider = f'https://api.themoviedb.org/3/movie/{movie_id}/watch/providers'



    res_details = requests.get(url_details, params=parameters)
    res_recommendations = requests.get(url_recommendations, params=parameters)
    res_similar = requests.get(url_similar, params=parameters)
    res_credits = requests.get(url_credits, params=parameters)
    res_videos = requests.get(url_videos, params=parameters)
    res_provider = requests.get(url_provider, params=parameters)

    results = {
        'details': res_details.json(),
        'recommendations': res_recommendations.json(),
        'similar': res_similar.json(),
        'credits': res_credits.json(),
        'videos': res_videos.json(),
        'providers': res_provider.json()
    }

    return results




















