from .db import db


class Leagues (db.Model):
    __tablename__ = "leagues"
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column('name', db.String(75))
    hashed_password = db.Column('hashed password', db.String(255))
    conference = db.Column('conference', db.Boolean)
    division = db.Column('division', db.Integer)
    commissioner = db.Column('commissioner', db.Integer, db.ForeignKey('users.id'))
    max_team = db.Column('max_team', db.Integer)

    users = db.relationship('Users', back_populates='leagues')


class PlayersLeagues (db.Model):
    __tablename__ = "players_leagues"
    playerid = db.Column('playerId', db.Integer, db.ForeignKey('players.id'), primary_key = True)
    leagueid = db.Column('leagueId', db.Integer, db.ForeignKey('leagues.id'), primary_key = True)

    players = db.relationship('Players', foreign_keys=playerid)
    leagues = db.relationship('Leagues', foreign_keys=leagueid)


class Schedule (db.Model):
    __tablename__ = "schedule"
    week = db.Column('week', db.Integer, primary_key = True)
    team_a_id = db.Column('team_a_id', db.Integer, db.ForeignKey('teams.id'), primary_key = True)
    team_b_id = db.Column('team_b_id', db.Integer, db.ForeignKey('teams.id'), primary_key = True)
    leagueid = db.Column('leagueId', db.Integer, db.ForeignKey('leagues.id'), primary_key = True)
    score_a = db.Column('score_a', db.Integer)
    score_b = db.Column('score_b', db.Integer)
    winner = db.Column('winner', db.String)

    teams = db.relationship('Teams', foreign_keys=team_a_id)
    teams = db.relationship('Teams', foreign_keys=team_b_id)
    leagues = db.relationship('Leagues', foreign_keys=leagueid)

