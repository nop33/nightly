from flask import Flask, render_template
from flask.ext import menu
from flask.ext.sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.jinja_env.globals.update(render_template=render_template)
db = SQLAlchemy(app)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('sass/_main.scss', filters='pyscss', output='css/main.css')
assets.register('scss_all', scss)

menu.Menu(app=app)

import nightly.controllers
