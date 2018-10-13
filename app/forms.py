from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, Required, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username    = StringField('Username', validators=[Required()])
    password    = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Remember me')
    submit      = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[Required()])
    email    = StringField('E-mail', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    password2 = PasswordField('Repeat Password', validators=[Required(), EqualTo('password')])
    submit   = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('E-mail already taken.')