from .db import db

class Teams (db.Model):
    __tablename__ = "teams"
    id = db.Column('id', db.Integer, primary_key = True)
    idp = db.Column('idp', db.Boolean)
    name = db.Column('name', db.String)
    leagueid = db.Column('leagueId', db.Integer, db.ForeignKey('leagues.id'))
    userid = db.Column('userId', db.Integer, db.ForeignKey('users.id'))
    proj_pts = db.Column('proj_pts', db.Integer)
    seas_pts = db.Column('seas_pts', db.Integer)
    abbr = db.Column('abbr', db.String)

    players = db.relationship('Players', back_populates='players')
    leagues = db.relationship('Leagues', foreign_keys=leagueid)
    users = db.relationship('Users', foreign_keys=userid)