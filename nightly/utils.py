import requests

from nightly import app


def get_movie_info(movie_id):
    api_key = app.config['TMDB_KEY']
    api_endpoint = app.config['TMDB_ENDPOINT']
    resp = requests.get('{}/movie/{}?api_key={}'.format(api_endpoint, movie_id, api_key))
    # TODO: Handle error responses better
    return resp.json() if resp.ok else False


def build_poster_url(poster_path=None):
    if poster_path:
        return '{}/{}'.format(app.config['TMDB_IMAGE_ENDPOINT'], poster_path)
    return 'http://placehold.it/500x750&text=Poster..+nah'
