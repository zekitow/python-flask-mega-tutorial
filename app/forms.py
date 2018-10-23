from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, Required, Email, EqualTo, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User

class LoginForm(FlaskForm):
    username    = StringField(_l('Username'), validators=[Required()])
    password    = PasswordField(_l('Password'), validators=[Required()])
    remember_me = BooleanField(_l('Remember me'))
    submit      = SubmitField(_l('Sign In'))

class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[Required()])
    email    = StringField(_l('E-mail'), validators=[Required(), Email()])
    password = PasswordField(_l('Password'), validators=[Required()])
    password2 = PasswordField(_l('Repeat Password'), validators=[Required(), EqualTo('password')])
    submit   = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_l('Username already taken.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_l('E-mail already taken.'))

class ResetPasswordRequestForm(FlaskForm):
    email  = StringField(_l('Email'), validators=[Required(), Email()])
    submit = SubmitField(_l('Request Password Reset'))

class ResetPasswordForm(FlaskForm):
    password  = PasswordField(_l('Password'), validators=[Required()])
    password2 = PasswordField(_l('Repeat Password'), validators=[Required(), EqualTo('password')])
    submit    = SubmitField(_l('Request Password Reset'))

class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[Required()])
    about_me = TextAreaField(_l('About me'), validators=[Length(min=0, max=140)])
    submit   = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_l('Please use a different username.'))

class PostForm(FlaskForm):
    post   = TextAreaField(_l('Say something'), validators=[Required(), Length(min=1, max=140)])
    submit = SubmitField(_l('Submit'))