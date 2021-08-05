from .db import db
from datetime import datetime
 

class Posts (db.Model):
    __tablename__ = "posts"
    id = db.Column('id', db.Integer, primary_key = True)
    title = db.Column('title', db.VARCHAR(50))
    body = db.Column('body', db.Text)
    created_at = db.Column('created_at', db.Date)
    userId = db.Column('userId', db.Integer, db.ForeignKey('users.id'))
    leagueId = db.Column('leagueId', db.Integer, db.ForeignKey('leagues.id'))
    index = db.Column('index', db.Integer)
    
    users = db.relationship('Users', foreign_keys=userId, back_populates="posts")
    comments = db.relationship('Comments', back_populates='posts')
    league = db.relationship('Leagues', foreign_keys=leagueId, back_populates="posts")

    def __init__(self, title, body, leagueId, userId, index):
        self.title = title
        self.body = body
        self.leagueId = leagueId
        self.userId = userId
        self.created_at = datetime.now(tz=None)
        # self.index = self.get_len_posts() + 1
        self.index = index

    @property
    def all_comments(self):
        return self.all_comments

    @all_comments.setter
    def all_comments(self):
        self.all_comments = self.all_comments_by_post()

    @property
    def pin(self):
        return self.pin

    @pin.setter
    def pin(self):
        self.pin = str(self.leagueId) + '-' + str(self.index)

    @classmethod
    def get_every_post(Class):
        all_posts = Class.query.all()
        return all_posts

    @classmethod
    def get_posts_by_league(Class, leagueId):
        leaguePosts = Class.query.order_by(Class.created_at).filter_by(leagueId=leagueId).all()
        return leaguePosts

    def get_len_posts(self):
        return len(self.get_posts_by_league(self.leagueId))

    @classmethod
    def get_posts_by_user(Class, userId):
        userPosts = Class.query.order_by(Class.created_at).filter_by(userId=userId).all()
        return userPosts

    def all_comments_by_post(self):
            all_comments = Comments.query.filter(Comments.postId == self.id).all()
            return all_comments

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'userId': self.userId,
            'createdAt': self.created_at,
            'all_comments': self.all_comments_by_post()
        }
    

class Comments (db.Model):
    __tablename__ = "comments"
    id = db.Column('id', db.Integer, primary_key = True)
    body = db.Column('body', db.Text)
    created_at = db.Column('created_at', db.Date)
    postId = db.Column('postId', db.Integer, db.ForeignKey('posts.id'))
    userId = db.Column('userId', db.Integer, db.ForeignKey('users.id'))
    index = db.Column('index', db.Integer)

    posts = db.relationship('Posts', foreign_keys=postId)
    users = db.relationship('Users', foreign_keys=userId)

    def __init__(self, body, postId, userId, index):
        self.body = body
        self.postId = postId
        self.userId = userId
        self.created_at = datetime.now(tz=None)
        # self.index = self.get_len_comments(self.postId)
        self.index = index


    @property
    def cin(self):
        return self.cin

    @cin.setter
    def cin(self):
        self.cin = str(self.get_parent_post().pin) + '-' + str(self.index)

    @classmethod
    def get_comments_by_post(Class, postId):
        all_comments = Class.query.filter_by(postId=postId).all()
        return all_comments
    @classmethod
    def get_len_comments(Class, postId):
        return Class.get_comments_by_post(postId)

    def get_parent_post(self):
        post = Posts.query.get(self.postId)
        return post

    def to_dict(self):
            return {
                'id': self.id,
                'postId': self.postId,
                'userId': self.userId,
                'body': self.body,
                'created_at': self.created_at,
            }
