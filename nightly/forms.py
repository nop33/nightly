from flask_wtf import Form
from wtforms import DateField, DateTimeField
from wtforms.validators import DataRequired
from wtforms.widgets.html5 import TimeInput


class MovieventForm(Form):
    date = DateField(
        'Date',
        validators=[DataRequired()],
        format='%d %B, %Y',
        description="Which day?"
    )
    time = DateTimeField(
        'Time',
        widget=TimeInput(),
        validators=[DataRequired()],
        format='%I:%M %p',
        description="and time?"
    )
