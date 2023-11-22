# forms.py
from flask_wtf import FlaskForm
from wtforms import DateField, DecimalField, IntegerField, SelectField, StringField, SubmitField, PasswordField, TextAreaField, TimeField
from wtforms.validators import DataRequired, Email, EqualTo, Length
import enum
class GENDER(enum.Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'

class CARE_TYPE(enum.Enum):
    babysitter = 'babysitter'
    caregiver_for_elderly = 'caregiver for elderly'
    playmate_for_children = 'playmate for children'

class STATUS(enum.Enum):
    accepted = 'accepted'
    declined = 'declined'
    pending = 'pending'

class UserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    given_name = StringField('Given Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    profile_description = TextAreaField('Profile Description', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])

# class CaregiverForm(FlaskForm):
#     photo = StringField('Photo URL', validators=[DataRequired()])
#     gender = SelectField('Gender', choices=[(gender.name, gender.value) for gender in GENDER], validators=[DataRequired()])
#     caregiving_type = SelectField('Caregiving Type', choices=[(care_type.name, care_type.value) for care_type in CARE_TYPE], validators=[DataRequired()])
#     hourly_rate = DecimalField('Hourly Rate', validators=[DataRequired()])

# class MemberForm(FlaskForm):
#     house_rules = TextAreaField('House Rules', validators=[DataRequired()])

# class AddressForm(FlaskForm):
#     house_number = StringField('House Number', validators=[DataRequired()])
#     street = StringField('Street', validators=[DataRequired()])
#     town = StringField('Town', validators=[DataRequired()])

# class JobForm(FlaskForm):
#     required_caregiving_type = SelectField('Required Caregiving Type', choices=[(care_type.name, care_type.value) for care_type in CARE_TYPE], validators=[DataRequired()])
#     other_requirements = TextAreaField('Other Requirements')
#     date_posted = DateField('Date Posted', validators=[DataRequired()])

# class JobApplicationForm(FlaskForm):
#     date_applied = DateField('Date Applied', validators=[DataRequired()])

# class AppointmentForm(FlaskForm):
#     appointment_date = DateField('Appointment Date', validators=[DataRequired()])
#     appointment_time = TimeField('Appointment Time', validators=[DataRequired()])
#     work_hours = IntegerField('Work Hours', validators=[DataRequired()])
#     status = SelectField('Status', choices=[(status.name, status.value) for status in STATUS], validators=[DataRequired()])
