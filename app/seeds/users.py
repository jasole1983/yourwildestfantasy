from app.models import db, Users
from app.models.rosters import NFL


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = Users(
        username='Demo', email='demo@aa.io', password='password')
    marnie = Users(
        username='marnie', email='marnie@aa.io', password='password')
    bobbie = Users(
        username='bobbie', email='bobbie@aa.io', password='password')

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)

    ARI = NFL(id=1, name="Arizona Cardinals",abbr="ARI", AFC=False, division="West " )
    ATL = NFL(id=2, name="Atlanta Falcons",abbr="ATL", AFC=False, division="South" )
    BAL = NFL(id=3, name="Baltimore Ravens",abbr="BAL", AFC=True, division="North")
    BUF = NFL(id=4, name="Buffalo Bills",abbr="BUF", AFC=True, division="East")
    CAR = NFL(id=5, name="Carolina Panthers",abbr="CAR", AFC=False, division="South")
    CHI = NFL(id=6, name="Chicago Bears",abbr="CHI", AFC=False, division="North")
    CIN = NFL(id=7, name="Cincinnati Bengals",abbr="CIN", AFC=True, division="North")
    CLE = NFL(id=8, name="Cleveland Browns",abbr="CLE", AFC=True, division="North")
    DAL = NFL(id=9, name="Dallas Cowboys",abbr="DAL", AFC=False, division="East")
    DEN = NFL(id=10, name="Denver Broncos",abbr="DEN", AFC=True, division="West")
    DET = NFL(id=11, name="Detroit Lions",abbr="DET", AFC=False, division="North")
    GB = NFL(id=12, name="Green Bay Packers",abbr="GB", AFC=False, division="North")
    HOU = NFL(id=13, name="Houston Texans",abbr="HOU", AFC=True, division="South")
    IND = NFL(id=14, name="Indianapolis Colts",abbr="IND", AFC=True, division="South")
    JAX = NFL(id=15, name="Jacksonville Jaguars",abbr="JAX", AFC=True, division="South") 
    KC = NFL(id=16, name="Kansas City Chiefs",abbr="KC", AFC=True, division="West")
    MIA = NFL(id=17, name="Miami Dolphins",abbr="MIA", AFC=True, division="East")
    MIN = NFL(id=18, name="Minnesota Vikings",abbr="MIN", AFC=False, division="North")
    NE = NFL(id=19, name="New England Patriots",abbr="NE", AFC=True, division="East")
    NO = NFL(id=20, name="New Orleans Saints",abbr="NO", AFC=False, division="South")
    NYG = NFL(id=21, name="NY Giants",abbr="NYG", AFC=False, division="East")
    NYJ = NFL(id=22, name="NY Jets",abbr="NYJ", AFC=True, division="East")
    LV = NFL(id=23, name="Las Vegas Raiders",abbr="LV", AFC=True, division="West")
    PHI = NFL(id=24, name="Philadelphia Eagles",abbr="PHI", AFC=False, division="East")
    PIT = NFL(id=25, name="Pittsburgh Steelers",abbr="PIT", AFC=True, division="North")
    LAC = NFL(id=26, name="Los Angeles Chargers",abbr="LAC", AFC=True, division="West")
    SF = NFL(id=27, name="San Francisco 49er",abbr="SF", AFC=False, division="West")
    SEA = NFL(id=28, name="Seattle Seahawks",abbr="SEA", AFC=False, division="West")
    LAR = NFL(id=29, name="Los Angeles Rams",abbr="LAR", AFC=False, division="West")
    TB = NFL(id=30, name="Tampa Bay Buccaneers",abbr="TB", AFC=False, division="South")
    TEN = NFL(id=31, name="Tennessee Titans",abbr="TEN", AFC=True, division="South")
    WAS = NFL(id=32, name="Washington Football Team",abbr="WAS", AFC=False, division="East")

    nflList = [
        ARI,
        ATL,
        BAL,
        BUF,
        CAR,
        CHI,
        CIN,
        CLE,
        DAL,
        DEN,
        DET,
        GB,
        HOU,
        IND,
        JAX,
        KC,
        MIA,
        MIN,
        NE,
        NO,
        NYG,
        NYJ,
        LV,
        PHI,
        PIT,
        LAC,
        SF,
        SEA,
        LAR,
        TB,
        TEN,
        WAS,
    ]
    db.session.add_all(nflList)

    db.session.commit()

    


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
