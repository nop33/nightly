from nightly import db


class Movie(db.Model):
    """A movie entry inside a Movievent"""

    __tablename__ = 'movies'
    __table_args__ = {'schema': 'nightly'}

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    tmdb_id = db.Column(
        db.Integer,
        nullable=False,
        index=True
    )
    title = db.Column(
        db.String,
        nullable=False,
        index=True
    )
    release_year = db.Column(
        db.Integer,
        nullable=True,
        index=True
    )
    poster_url = db.Column(
        db.String,
        nullable=True
    )
    movievent_id = db.Column(
        db.Integer,
        db.ForeignKey('nightly.movievents.id'),
        nullable=False
    )

    # relationship backrefs:
    # - movievent (Movievents.movies)

    def __repr__(self):
        return '<Movie({}, {}, {})>'.format(self.id, self.tmdb_id, self.title)


class Movievent(db.Model):
    """Represents an event"""

    __tablename__ = 'movievents'
    __table_args__ = {'schema': 'nightly'}

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    date = db.Column(
        db.Date,
        nullable=False
    )
    time = db.Column(
        db.DateTime,
        nullable=False
    )
    movies = db.relationship(
        'Movie',
        backref='movievent',
        cascade='all, delete-orphan',
        primaryjoin=(id == Movie.movievent_id)
    )

    def __repr__(self):
        return '<Movievent({}, {})>'.format(self.id, self.date)
