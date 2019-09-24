from flask_wtf import FlaskForm
from app.models import Reunion
from wtforms import SelectField


class TurfForm(FlaskForm):
    date = SelectField('date', choices=[])
    hippodrome = SelectField('hippodrome', choices=[])

