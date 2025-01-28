from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired

class UserData(FlaskForm):
    user = StringField('Username  :', validators=[InputRequired()])
    pwd = PasswordField('Password    :', validators=[InputRequired()])
    submit = SubmitField('Login')