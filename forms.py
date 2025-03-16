from wtforms import *
from flask_wtf import *
from wtforms.validators import *
from our_requests import *

class InventoryaddForm(FlaskForm):
    name = StringField("Ссылка на ресурс", validators=[DataRequired()])
    submit = SubmitField("Ввести")