from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    pronouns = SelectField('Pronouns', choices=[(None, 'Pronouns'),('She/Her', 'She/Her'), ('He/Him', 'He/Him'), ('They/Them', 'They/Them')])
    avatar = SelectField(u'Choose Your Avatar', choices=[(None,'Avatar'),('d', 'Dog'), ('c', 'Cat'), ('s', 'Sunset')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class CommentForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    comment = StringField('Comment',
                        validators=[DataRequired(), Length(min=1, max=255)])
    submit = SubmitField('Post Comment')