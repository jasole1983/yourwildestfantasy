from .db import db
 

class Posts (db.Model):
    __tablename__ = "posts"
    id = db.Column('id', db.Integer, primary_key = True)
    title = db.Column('title', db.VARCHAR(79))
    body = db.Column('body', db.Text)
    created_at = db.Column('created_at', db.Date)
    userId = db.Column('userId', db.Integer, db.ForeignKey('users.id'))

    users = db.relationship('Users', foreign_keys=userId, back_populates="posts")
    comments = db.relationship('Comments', back_populates='posts')

    @property
    def all_comments(self):
        return self.all_comments

    @all_comments.setter
    def all_comments(self):
        self.all_comments = self.all_comments_by_post()

    def all_comments_by_post(self):
            all_comments = Comments.query.all().filter(self.id)
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

    posts = db.relationship('Posts', foreign_keys=postId)
    users = db.relationship('Users', foreign_keys=userId)

    def to_dict(self):
            return {
                'id': self.id,
                'postId': self.postId,
                'userId': self.userId,
                'body': self.body,
                'created_at': self.created_at,
            }