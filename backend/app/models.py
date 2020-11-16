#"Data models.""
from . import db
from datetime import datetime
from sqlalchemy_utils.types.choice import ChoiceType
from sqlalchemy import *

#"Data model for user accounts."
class User(db.Model):
    TYPES = [
        (u'admin', u'Admin'),
        (u'member', u'Member'),
        (u'applicant', u'Applicant'),
        (u'admin-applicant', u'Admin-Applicant')
    ]

    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)  
    user_groups = db.Table('user_groups',
    db.Column('left_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('right_id', db.Integer, db.ForeignKey('groups.id')),
    db.Column('tokens_left',db.VARBINARY(150)),
    db.Column('role', ChoiceType(TYPES), default='member')
    )

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)


#"Data models for groups."
class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    tokens = db.Column(db.Integer(), nullable=False, default = 0)
    #group_user_type = db.Table('group_user_type',
    #db.Column('group_id', db.Integer, db.ForeignKey('groups.id')),
    #db.Column('user_role',ChoiceType(TYPES), db.ForeignKey('user_groups.role'))
    #)
    poll = db.relationship('Poll', backref='groups', lazy=True)
        

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)


#"Data models for poll."
class Poll(db.Model):
    __tablename__ = 'polls'
    id = db.Column(db.Integer(), primary_key=True)
    question = db.Column(db.Text(), nullable=False)
    start_time = db.Column(db.DateTime(), default=datetime.utcnow)
    end_time =  db.Column(db.DateTime(), default=datetime.utcnow)
    result = db.Column(db.String(50), nullable=False)
    group = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    options = db.relationship('Option', backref='polls', lazy=True)
    votes = db.Table('votes',
    db.Column('left_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('right_id', db.Integer, db.ForeignKey('groups.id')),
    db.Column('vote',db.VARBINARY(150))
    )

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.question)


#"Data models for options in a poll."
class Option(db.Model):
    __tablename__ = 'options'
    id = db.Column(db.Integer(), primary_key=True)
    option_description = db.Column(db.Text(), nullable=False)
    poll = db.Column(db.Integer, db.ForeignKey('polls.id'), nullable=False)
        

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.option_description)

