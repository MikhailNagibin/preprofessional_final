from wtforms import *
from flask_wtf import *
from wtforms.validators import *
from our_requests import *

class InputlinkForm(FlaskForm):
    name = StringField("Ссылка на ресурс", validators=[DataRequired()])
    submit = SubmitField("Ввести")

class MapviewForm(FlaskForm):
    base = SubmitField("Просмотр базовых станций")
    rad = SubmitField("Просмотр радиусов станций")
    isled = SubmitField("Просмотр исследовательских станций")