from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, Date, Time, DECIMAL, CheckConstraint
from sqlalchemy.orm import relationship

from flaskApp import db
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

# Models
class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    given_name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    profile_description = db.Column(db.Text, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    
# class Caregiver(db.Model):
#     __tablename__ = 'caregiver'

#     caregiver_user_id = Column(Integer, ForeignKey('user.user_id', ondelete='CASCADE'), primary_key=True)
#     photo = Column(String(255) , nullable=False)
#     gender = Column(Enum(GENDER) , nullable=False)
#     caregiving_type = Column(Enum(CARE_TYPE), nullable=False)
#     hourly_rate = Column(DECIMAL(10, 2), nullable=False)

#     user = relationship("User")

# class Member(db.Model):
#     __tablename__ = 'member'

#     member_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), primary_key=True)
#     house_rules = db.Column(db.Text, nullable=False)

#     user = relationship("User", back_populates="member")


# class Address(db.Model):
#     __tablename__ = 'address'

#     member_user_id = Column(Integer, ForeignKey('member.member_user_id', ondelete='CASCADE'), primary_key=True)
#     house_number = Column(String(10), nullable=False)
#     street = Column(String(100), nullable=False)
#     town = Column(String(50), nullable=False)
#     member = relationship("Member")

# class Job(db.Model):
#     __tablename__ = 'job'

#     job_id = Column(Integer, primary_key=True)
#     member_user_id = Column(Integer, ForeignKey('member.member_user_id', ondelete='CASCADE'), nullable=False)
#     required_caregiving_type = Column(Enum(CARE_TYPE, name='care_type_enum'), nullable=False)
#     other_requirements = Column(Text)
#     date_posted = Column(Date, nullable=False)

#     member = relationship("Member")


# class JobApplication(db.Model):
#     __tablename__ = 'job_application'

#     caregiver_user_id = Column(Integer, ForeignKey('caregiver.caregiver_user_id', ondelete='CASCADE'), primary_key=True)
#     job_id = Column(Integer, ForeignKey('job.job_id', ondelete='CASCADE'), primary_key=True)
#     date_applied = Column(Date,  nullable=False)

#     caregiver = relationship("Caregiver")
#     job = relationship("Job")

# class Appointment(db.Model):
#     __tablename__ = 'appointment'

#     appointment_id = Column(Integer, primary_key=True)
#     caregiver_user_id = Column(Integer, ForeignKey('caregiver.caregiver_user_id', ondelete='CASCADE'), nullable=False)
#     member_user_id = Column(Integer, ForeignKey('member.member_user_id', ondelete='CASCADE'), nullable=False)
#     appointment_date = Column(Date, nullable=False)
#     appointment_time = Column(Time, nullable=False)
#     work_hours = Column(Integer, CheckConstraint('work_hours > 0'), nullable=False)
#     status = Column(Enum(STATUS, name='status_enum'), nullable=False, default=STATUS.pending.value)

#     caregiver = relationship("Caregiver")
#     member = relationship("Member")
