from app.models import db, Posts, Comments, Leagues

def seed_posts():

    demoLeague = Leagues(
       name="new Super Fun League", conference=False, division=2, max_roster=12, userId=2, commissioner=2, idp=False, hashed_password=None, id=1
    )

    firstP = Posts(
        title='FIRST', body='the first attempt', leagueId=1, userId=2, index=1
    )
    secondP = Posts(
        title='SECOND', body='here I go again, trying a second time', leagueId=1, userId=2, index=2
    )
    thirdP = Posts(
        title='THIRD', body='and again and again', leagueId=1, userId=2, index=3
    )
    fourP = Posts(
        title='FOURTH', body='oh my goodness, still?', leagueId=1, userId=2, index=4
    )
    fireP = Posts(
        title='FIFTH', body='would you look at athat', leagueId=1, userId=2, index=5
    )
    f6P = Posts(
        title='SIXTH', body='I guess I will try one more time', leagueId=1, userId=2, index=6
    )
    lastP = Posts(
        title='SEVENTH', body='Okie dokie, I am done with these attempts', leagueId=1, userId=2, index=7
    )

    items_to_seed = [
        firstP, secondP, thirdP, fourP, fireP, f6P, lastP, 
    ]

    db.session.add(demoLeague)
    db.session.add_all(items_to_seed)
    db.session.commit()

def seed_comments():

    oneone = Comments(
        body='witty comment the first', postId=1, userId=2, index=1
    )
    onetwo = Comments(
        body="witty comment the second", postId=1, userId=2, index=2
    )
    onethree = Comments(
        body='and again with the wit', postId=1, userId=2, index=3
    )
    threeone = Comments(
        body='serious commenting here', postId=3, userId=1, index=1
    )
    threetwo = Comments(
        body='oh my, lighten up sourpuss', postId=3, userId=1, index=2
    )
    threethree = Comments(
        body='well, I never!', postId=3, userId=2, index=3
    )
    threefour = Comments(
        body='that explains a whole lot...', postId=3, userId=3, index=4
    )
    
    listOfStuff = [
        oneone, onetwo, onethree, threeone, threetwo, threethree, threefour
    ]
 
    db.session.add_all(listOfStuff)


    db.session.commit()




def undo_posts():
        db.session.execute('TRUNCATE leagues RESTART IDENTITY CASCADE;')
        db.session.execute('TRUNCATE posts RESTART IDENTITY CASCADE;')
        
        db.session.commit()
        
def undo_comments():        
        db.session.execute('TRUNCATE comments RESTART IDENTITY CASCADE;')
        db.session.commit()