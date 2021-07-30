from .db import db
from .user import Users 

class Posts (db.Model):
    __tablename__ = "posts"
    id = db.Column('id', db.Integer, primary_key = True)
    post = db.Column('post', db.Text),
    created_at = db.Column('created_at', db.Timestampz)
    userId = db.Column('userId', db.Integer, db.ForeignKey('users.id'))

    users = db.relationship('Users', foreign_keys=userid, back_populates="posts")

    def to_dict(self):
        user = Users.query.get(self.userId)
        return {
            'id': self.id,
            'post': self.post,
            'user': user.username,
            'userId': self.userId,
            'createdAt': self.created_at
        }


class Comments (Posts, db.Model):
    __tablename__ = "comments"
    id = db.Column('id', db.Integer, primary_key = True)
    comment = db.Column('comment', db.Text)
    postid = db.Column('postId', db.Integer, db.ForeignKey('posts.id'))
    userid = db.Column('userId', db.Integer, db.ForeignKey('users.id'))

    posts = db.relationship('Posts', foreign_keys=postid)
    users = db.relationship('Users', foreign_keys=userid)


    def to_dict(self):
            
