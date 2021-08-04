from app.api.auth_routes import validation_errors_to_error_messages
from flask import Blueprint, jsonify, session, request
from flask_login import login_required, current_user
from app.models import Posts, Comments, db
from app.forms import NewPost, NewComment

post_routes = Blueprint('posts', __name__)
comment_routes = Blueprint('comments', __name__)


@post_routes.route('/')
@login_required
def all_posts():
    '''
    GET route to retreive all possible posts --> likely superfluous for Production
    '''
    posts = Posts.query.all()
    return {'posts': [post.to_dict() for post in posts]}

@post_routes.route('/<int:leagueid>')
@login_required
def posts_by_league(leagueid):
    '''
    GET all posts associated w/ a specific league
    '''
    leaguePosts = Posts.get_posts_by_league(leagueid)
    return {'posts': [post.to_dict() for post in leaguePosts]}

@post_routes.route('/league/<int:leagueid>', methods=['POST'])
@login_required
def create_new_post(leagueid):
    '''
    POST route to create new message on league board
    '''
    form = NewPost()
    form['csrf_token'].data = request.cookies['csrf_token']
    if request.method == 'POST' and form.validate_on_submit:
        post = Posts()
        form.populate_obj(post)
        db.session.add(post)
        db.session.commit()
        return {'post': post.to_dict()}
    else:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@post_routes.route('/<int:postid>', methods=['GET'])
@login_required
def get_this_post(postid):
    post = Posts.query.get(postid)
    if post:
        return {'post': post.to_dict()}

@post_routes.route('/<int:postid>', methods=['PUT'])
@login_required
def alter_post(postid):
    '''
    PUT route to handle editing a post
    '''
    post = Posts.query.get(postid)
    form = NewPost()
    form['csrf_token'].data = request.cookies['csrf_token']
    if request.method == 'PUT' and form.validate_on_submit:
        for key, value in request.form:
            setattr(post, key, value)
        db.session.commit()
        return {'post': post.to_dict()}
    else:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@post_routes.route('/<int:postid>', methods=['DELETE'])
@login_required
def delete_post(postid):
    '''
    DELETE route to remove a post
    '''
    form = NewPost()
    post = Posts.query.get(postid)
    if post.userId == current_user.id and request.method == 'DELETE':
        postCopy = {k:v for k,v in post}
        db.session.delete(post)
        db.session.commit()
        return {'post': post.to_dict()}
    else:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@comment_routes.route('/<int:postid>/comments/<int:commentid>', methods=['GET'])
@login_required
def get_comment(postid, commentid):
    '''
    GET specific comment by id
    '''
    comment = Comments.query.get(commentid)
    if comment.userId == current_user.idk and comment.postId == postid:
        return {'comment':comment.to_dict()}
    else:
        return {'errors': "incorrect commentId or postId"}
