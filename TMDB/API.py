import requests
from common_utils.variables import API_KEY

def getGenreList(language='en-US'):
    parameters = {'api_key': API_KEY, 'language': language}
    url_movie = 'https://api.themoviedb.org/3/genre/movie/list'
    url_show = 'https://api.themoviedb.org/3/genre/tv/list'

    results = {
        'movies': requests.get(url_movie, params=parameters).json(),
        'shows': requests.get(url_show, params=parameters).json()
    }

    return results


def getMovieVideosLinks(movie_id):
    if not movie_id:
        return []

    return [
        f'https://vidsrc.icu/embed/movie/{movie_id}',
        f'https://vidsrc.xyz/embed/movie/{movie_id}',
        f'https://embed.su/embed/movie/{movie_id}'
    ]


def getShowVideoLinks(tv_id, season_number, episode_number):
    if not tv_id or not season_number or not episode_number:
        return []

    return [
        f'https://vidsrc.icu/embed/tv/{tv_id}/{season_number}/{episode_number}',
        f'https://vidsrc.xyz/embed/tv/{tv_id}/{season_number}-{episode_number}',
        f'https://embed.su/embed/tv/{tv_id}/{season_number}/{episode_number}'
    ]
