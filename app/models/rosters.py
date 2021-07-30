from .db import db

class RosterPositionSettings (db.Model):
    __tablename__ = "roster_position_settings"
    id = db.Column('id', db.Integer, primary_key = True)
    leagueid = db.Column('leagueId', db.Integer, db.ForeignKey('leagues.id'))

    leagues = db.relationship('Leagues', foreign_keys=leagueid)

    
class Players (db.Model):
    __tablename__ = "players"
    id = db.Column('id', db.Integer, primary_key = True)
    firstname = db.Column('firstName', db.String)
    lastname = db.Column('lastName', db.String)

offPositions = ENUM("QB", "RB", "WR", "TE", "DST", "K", name="offensivePositions", metadata=metadata)
defPositions = ENUM("DL", "DT", "DE", "LB", "OLB", "MLB", "DB", "FS", "SS", "S", "CB", name="defensivPositions", metadata=metadata)
plyrStatus = ENUM("IR", "R", "FA", "D", "P", "S", "HO", "COV", "LOK", name="playerStatus", metadata=metadata)
conferences = ENUM("AFC", "NFC", name="conference", metadata=metadata)
divisions = ENUM("WEST", "SOUTH", "EAST", "NORTH", name="divisions", metadata=metadata)