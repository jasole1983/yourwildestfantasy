import os
# from sqlalchemy import create_engine


class Config:
    SECRET_KEY = "lkasjdf09ajsdkfljalsiorj12n3490re9485309irefvn,u90818734902139489230"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLAlchemy 1.4 no longer supports url strings that start with 'postgres'
    # (only 'postgresql') but heroku's postgres add-on automatically sets the
    # url in the hidden config vars to start with postgres.
    # so the connection uri must be updated here
    SQLALCHEMY_DATABASE_URI = "postgresql://fantasy_app:password@localhost/wild_fantasy"
    SQLALCHEMY_ECHO = True

# db_url = Config.SQLALCHEMY_DATABASE_URI
# eng = create_engine(db_url)

