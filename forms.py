from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    username = StringField('UserName', validators = [ DataRequired])
