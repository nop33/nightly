from app import db


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

    def __repr__(self):
        return '<Movievent({id}, {date})>'.format(id=self.id, date=self.date)
