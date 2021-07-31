from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Users (UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column('id', db.Integer, primary_key = True)
    username = db.Column('username', db.String)
    full_name = db.Column('full_name', db.String)
    email = db.Column('email', db.String)
    hashed_password = db.Column('hashed_password', db.String)

    leagues = db.relationship('Leagues', back_populates='users' )
    posts = db.relationship('Posts', back_populates='users')
    comments = db.relationship('Comments', back_populates='users')

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'leagues': self.leagues,
            'posts': self.posts,
            'comments': self.comments,
        }


class UsersLeagues (db.Model):
    __tablename__ = "users_leagues"
    userid = db.Column('userId', db.Integer, db.ForeignKey('users.id'), primary_key = True)
    leagueid = db.Column('leagueId', db.Integer, db.ForeignKey('leagues.id'), primary_key = True)

    users = db.relationship('Users', foreign_keys=userid)
    leagues = db.relationship('Leagues', foreign_keys=leagueid)