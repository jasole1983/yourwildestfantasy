from .db import db

class Posts (db.Model):
    __tablename__ = "posts"
    id = db.Column('id', db.Integer, primary_key = True)
    post = db.Column('post', db.Text),
    created_at = db.Column('created_at', db.Timestampz)
    updated_at = db.Column('updated_at', db.Timestampz)
    userid = db.Column('userId', db.Integer, db.ForeignKey('users.id'))

    users = db.relationship('Users', foreign_keys=userid)

class Comments (Posts, db.Model):
    __tablename__ = "comments"
    id = db.Column('id', db.Integer, primary_key = True)
    comment = db.Column('comment', db.Text)
    postid = db.Column('postId', db.Integer, db.ForeignKey('posts.id'))
    userid = db.Column('userId', db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column('created_at', db.TimeStampz)
    updated_at = db.Column('updated_at', db.TimeStampz)

    posts = db.relationship('Posts', foreign_keys=postid)
    users = db.relationship('Users', foreign_keys=userid)
