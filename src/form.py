from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class UserData(FlaskForm):
    user = StringField('Username')
    pwd = StringField('Password')
    submit = SubmitField('Login')