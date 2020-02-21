from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, required, length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    name = StringField('Whats your name', validators=[DataRequired(), length(3, 15, message='between 3 to 15 characters')])
    email = StringField('Enter your Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), length(5), EqualTo('conform', message='Password must match')])
    confirm = PasswordField('Confirm your password', validators=[DataRequired()])
    submit = SubmitField('Register')
