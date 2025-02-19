import requests

from common_utils.variables import API_KEY


def getMovieDiscover(language='en-US', sort_by='popularity.desc', page=1, vote_average=5, vote_sort='gte', with_genres='', include_adult=False, include_video=False):
    parameters = {'api_key': API_KEY, 'language': language,
                  'page': page, 'sort_by': sort_by, f'vote_average.{vote_sort}': vote_average, 'with_genres': with_genres, 
                  "include_adult": include_adult, "include_video": include_video}
    url = 'https://api.themoviedb.org/3/discover/movie'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getTVShowsDiscover(language='en-US', sort_by='popularity.desc', page=1, vote_average=5, vote_sort='gte', with_genres='', with_networks='', include_adult=False):
    parameters = {'api_key': API_KEY, 'language': language,
                  'page': page, 'sort_by': sort_by, f'vote_average.{vote_sort}': vote_average, 'with_genres': with_genres, 
                  'with_networks': with_networks, "include_adult": include_adult}

    url = 'https://api.themoviedb.org/3/discover/tv'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getPopularMovies(language='en-US', page=1):
    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = 'https://api.themoviedb.org/3/movie/popular'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getVideos(movie_id, language='en-US'):
    parameters = {'api_key': API_KEY, 'language': language}
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results