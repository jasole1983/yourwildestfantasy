from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Leagues (UserMixin, db.Model):
    __tablename__ = "leagues"
    id = db.Column('id', db.Integer, primary_key = True)
    idp = db.Column('idp', db.Boolean)
    name = db.Column('name', db.String(75))
    hashed_password = db.Column('hashed password', db.String(255))
    conference = db.Column('conference', db.Boolean)
    division = db.Column('division', db.Integer)
    max_roster = db.Column('max_roster', db.Integer)
    userId = db.Column('userId', db.Integer, db.ForeignKey('users.id'))
    commissioner = db.Column('commissioner', db.Integer)

    players = db.relationship('Players', back_populates='league')
    users = db.relationship('Users', back_populates='leagues')
    posts = db.relationship('Posts', back_populates='league')

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_att}

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'conference': self.conference,
    #         'division': self.division,
    #         'max_roster': self.max_roster,
    #         'userId': self.userId,
    #     }


class PlayersLeagues (db.Model):
    __tablename__ = "players_leagues"
    playerId = db.Column('playerId', db.Integer, db.ForeignKey('players.id'), primary_key = True)
    leagueId = db.Column('leagueId', db.Integer, db.ForeignKey('leagues.id'), primary_key = True)

    players = db.relationship('Players', foreign_keys=playerId)
    leagues = db.relationship('Leagues', foreign_keys=leagueId)


class Schedule (db.Model):
    __tablename__ = "schedule"
    week = db.Column('week', db.Integer, primary_key = True)
    leagueId = db.Column('leagueId', db.Integer, db.ForeignKey('leagues.id'), primary_key = True)
    home_roster_id = db.Column('home_roster_id', db.Integer, db.ForeignKey('rosters.id'), primary_key = True)
    away_roster_id = db.Column('away_roster_id', db.Integer, db.ForeignKey('rosters.id'))
    home_score = db.Column('home_score', db.Integer)
    away_score = db.Column('away_score', db.Integer)
    home_wins = db.Column('home_wins', db.Boolean, nullable=True)

    home = db.relationship('Rosters', foreign_keys=home_roster_id)
    away = db.relationship('Rosters', foreign_keys=away_roster_id)
    
    # def to_dict_by_week(self, leagueId, week):
    #     thisWeek = Schedule.query.filter_by(leagueId == self.leaguId, self.week == week).all()
    #     return {
    #         f'(self.leagueId)_(self.week)': {f'(match.home_roster_id)_(match.away_roster_id)':match for f'(match.home_roster_id)_(match.away_roster_id)',match in thisWeek}
    #     }
    def to_dict(self):
        return {
            'week': self.week,
            'leagueId': self.leagueId,
            'homeRosterId': self.home_roster_id,
            'awayRosterId': self.away_roster_id,
            'homeScore': self.home_score,
            'awayScore': self.away_score,
            'homeWins': self.home_wins,
        }




