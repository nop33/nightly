import requests

from flask import render_template, flash, redirect, url_for, request, jsonify

from nightly import app, db, menu
from nightly.forms import MovieventForm
from nightly.models import Movievent, Movie
from nightly.utils import get_movie_info, build_poster_url


@app.route('/')
@menu.register_menu(app, '.home', 'Home', order=0)
def home():
    return render_template('pages/home.html')


@app.route('/movievents')
@menu.register_menu(app, '.movievents', 'Movievents', order=5)
def movievents():
    movievents = Movievent.query.order_by("date desc").order_by("time desc").all()
    return render_template('pages/movievents.html', movievents=movievents)


@app.route('/movievent/create', methods=('GET', 'POST'))
def movievent_create():
    form = MovieventForm()
    if form.validate_on_submit():
        movievent = Movievent()
        form.populate_obj(movievent)
        db.session.add(movievent)
        db.session.commit()
        flash('Movievent created successfully', 'success')
        return redirect(url_for('.movievent', id=movievent.id))
    return render_template('pages/movievent_create.html', form=form)


@app.route('/movievent/<int:id>/save-movies', methods=('GET', 'POST'))
def movievent_save_movies(id):
    movies = request.json
    for movie_id in movies:
        movie = get_movie_info(movie_id)
        if movie:
            if Movie.query.filter_by(tmdb_id=movie_id).count():
                continue
            m = Movie(tmdb_id=movie_id, title=movie['title'])
            m.release_year = int(movie.get('release_date')[0:4])
            m.poster_url = build_poster_url(movie.get('poster_path'))
            movievent = Movievent.query.filter_by(id=id).first()
            movievent.movies.append(m)
            db.session.commit()
    template = app.jinja_env.get_or_select_template('helpers/macros.html')
    tpl = template.make_module()
    success_message = tpl.render_flash_messages('positive', ['The movies were successfully saved!'])
    return jsonify(success_message=success_message)


@app.route('/movievent/<int:id>')
def movievent(id):
    movievent = Movievent.query.filter_by(id=id).first_or_404()
    return render_template('pages/movievent.html', movievent=movievent)


@app.route('/search/movies', methods=('POST',))
def search_movies():
    keyword = request.values.get('keyword')
    if not keyword:
        return
    api_key = app.config['TMDB_KEY']
    api_endpoint = app.config['TMDB_ENDPOINT']
    resp = requests.get('{}/search/movie?api_key={}&query={}'.format(api_endpoint, api_key, keyword))
    json_results = resp.json()
    return jsonify(json_results)


@app.route('/search/movie', methods=('POST',))
def search_movie():
    movie_id = request.values.get('id')
    if not movie_id:
        return
    movie = get_movie_info(movie_id)
    if not movie:
        return
    title = movie.get('title')
    moviecard = {'tmdb_id': movie_id,
                 'title': (title[:20] + '..') if len(title) > 20 else title,
                 'release_year': movie.get('release_date')[0:4],
                 'poster_url': build_poster_url(movie.get('poster_path'))}
    return render_template('pages/moviecard.html', movie=moviecard)
# @app.route('/')
# def hello():
#     return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
