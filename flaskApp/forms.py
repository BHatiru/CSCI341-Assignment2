# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField

class UserForm(FlaskForm):
    given_name = StringField('Given Name')
    surname = StringField('Surname')
    email = StringField('Email')
    password = PasswordField('Password')
    city = StringField('City')
    phone_number = StringField('Phone Number')
    profile_description = TextAreaField('Profile Description')
