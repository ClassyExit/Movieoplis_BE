import requests


from common_utils.variables import API_KEY


def multiSearch(query, language='en-US', page=1):
    if not query:
        return 'Missing query search'

    parameters = {'api_key': API_KEY,
                  'language': language, 'query': query, 'page': page}
    url_tv = f'https://api.themoviedb.org/3/search/tv'
    url_movie = f'https://api.themoviedb.org/3/search/movie'

    try:
        results_tv = requests.get(url_tv, params=parameters).json()
        results_movie = requests.get(url_movie, params=parameters).json()
    except requests.exceptions.RequestException as e:
        return {'error': f'API request failed: {str(e)}'}


    # Ensure 'results' key exists
    results_tv_list = results_tv.get('results', [])
    results_movie_list = results_movie.get('results', [])
    

    for show in results_tv_list:
        # Add in 'type' field 
        show['type'] = 'tv'

    for movie in results_movie_list:
        # Add in 'type' field 
        movie['type'] = 'movie'

    
    results = {
        'results': results_tv_list + results_movie_list
    }

    return results

