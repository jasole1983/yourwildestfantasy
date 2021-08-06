from .db import db


class RosterPositionSettings (db.Model):
    __tablename__ = "roster_position_settings"
    id = db.Column('id', db.Integer, primary_key = True)
    leagueId = db.Column('leagueId', db.Integer, db.ForeignKey('leagues.id'))
    position = db.Column('position', db.VARCHAR(3))
    min_start = db.Column('min_start', db.Integer)
    max_start = db.Column('max_start', db.Integer)
    min_rost = db.Column('min_rost', db.Integer)
    max_rost = db.Column('max_rost', db.Integer)

    leagues = db.relationship('Leagues', foreign_keys=leagueId)

    def get_lg_settings(self, leagueId):
        leagueSettings = RosterPositionSettings.query.filter_by(leagueId == self.leagueId).all()
        return[{setting.position: {
                                'min_start': setting.min_start,
                                'max_start': setting.max_start,
                                'min_rest': setting.min_rost,
                                'max_rest': setting.max_rost,
                                }} for setting in leagueSettings]

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'leagueId': self.leagueId,
    #         'position': self.position,
    #         self.position: {
    #                     'min_start': self.min_start,
    #                     'max_start': self.max_start,
    #                     'min_rost': self.min_rost,
    #                     'max_rost': self.max_rost,
    #                     }
    #     }


class Rosters (db.Model):
    __tablename__ = "rosters"
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column('name', db.String)
    leagueId = db.Column('leagueId', db.Integer, db.ForeignKey('leagues.id'))
    userId = db.Column('userId', db.Integer, db.ForeignKey('users.id'))
    proj_pts = db.Column('proj_pts', db.Integer)
    seas_pts = db.Column('seas_pts', db.Integer)
    abbr = db.Column('abbr', db.VARCHAR(5))

    leagues = db.relationship('Leagues', foreign_keys=leagueId)
    users = db.relationship('Users', foreign_keys=userId, back_populates='rosters')

    def to_dict(self):
        players = Players.query.filter(Players.rosterId == self.rosterId).all()
        return {
            'id': self.id,
            'name': self.name,
            'leagueId': self.leagueId,
            'userId': self.userId,
            'proj_pts': self.proj_pts,
            'seas_pts': self.seas_pts,
            'abbr': self.abbr,
            'players': players,
        }

class Players (db.Model):
    __tablename__ = "players"
    id = db.Column('id', db.Integer, primary_key = True)
    firstName = db.Column('firstName', db.String(50))
    lastName = db.Column('lastName', db.String(50))
    position = db.Column('position', db.String(3))
    age = db.Column('age', db.Integer)
    NFL_id = db.Column('NFL_Team', db.ForeignKey('NFL.id'))
    seasons = db.Column('seasons', db.Integer)
    status = db.Column('status', db.VARCHAR(3))
    current_season_pts = db.Column('current_season_pts', db.Integer)
    career_pts = db.Column('career_pts', db.Integer)
    projected_pts = db.Column('projected_pts', db.Integer)
    rosterId = db.Column('rosterId', db.Integer, db.ForeignKey('rosters.id')) 
    leagueId = db.Column('leagueId', db.Integer, db.ForeignKey('leagues.id'))

    NFL = db.relationship('NFL', foreign_keys=NFL_id)
    league = db.relationship('Leagues', foreign_keys=leagueId, back_populates='players')

    def to_dict(self):
        NFL_team = NFL.query.get(self.NFL_id)
        roster = Rosters.query.get(self.rosterId)
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'position': self.position,
            'age': self.age,
            'NFL': NFL_team.abbr,
            'seasons': self.seasons,
            'status': self.status,
            'currentPts': self.current_season_pts,
            'careerPts': self.career_pts,
            'projectedPts': self.projected_pts,
            'roster': roster.abbr,
            'leagueId': self.leagueId,            
        }


class NFL (db.Model):
    __tablename__ = "NFL"
    id = db.Column('id', db.Integer, primary_key = True)
    AFC = db.Column('AFC', db.BOOLEAN) 
    division = db.Column('division', db.VARCHAR(5))
    name = db.Column('name', db.VARCHAR(30))
    abbr = db.Column('abbr', db.VARCHAR(3))

    def to_dict(self):
        return {
            'id': self.id,
            'conference': self.AFC,
            'division': self.division,
            'name': self.team_name,
            'abbr': self.abbr,
        }