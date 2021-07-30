
from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.ext.automap import automap_base
engine = create_engine("postgresql://wild_fantasy_app:y0Urf4n74C@localhost:5000/your_wild_fantasy")

# produce our own MetaData object
metadata = MetaData()

# we can reflect it ourselves from a database, using options
# such as 'only' to limit what tables we look at...
metadata.reflect(engine)


Base = automap_base(metadata=metadata)

Base.prepare()

# mapped classes are ready
[print(model) for model in Base.classes]








# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine


# Base = automap_base()

# eng = create_engine("postgresql://wild_fantasy_app:y0Urf4n74C@localhost:5000/your_wild_fantasy")

# Base.prepare(eng, reflect=True)

# User = Base.classes.user
# RostPosSet = Base.classes.rost_pos_set
# League = Base.classes.leagues
# Team = Base.classes.teams
# Schedule = Base.classes.schedule
# Post = Base.classes.posts
# Comment = Base.classes.comment
# Player = Base.classes.players
# NFL_Taam = Base.classes.NFL_Teams

# session = Session(eng)

# print(u1.rost_pos_set_collection)
