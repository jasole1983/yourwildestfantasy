from wtforms import TextAreaField, validators, StringField, SubmitField, IntegerField
from flask_wtf import Form 
from wtforms import ValidationError
from wtforms.fields.simple import HiddenField
from wtforms.validators import DataRequired, InputRequired

class NewPost(Form):
    title =  StringField(u'Title', validators=[validators.InputRequired()])
    body = TextAreaField(u'Body', validators=[validators.InputRequired()])
    userId = HiddenField('User', validators=[validators.InputRequired()])
    leagueId= HiddenField('League', validators=[validators.InputRequired()])
    index = HiddenField('Index', validators=[validators.InputRequired()])

    def validate_body(form, field):
        if len(field.data) > 1000:
            raise ValidationError("1000 character limit exceeded")

    def validate_title(form, field):
        if len(field.data) > 50:
            raise ValidationError("50 character limit exceeded")



class NewComment(Form):
    postId = HiddenField('Post', validators=[validators.InputRequired()])
    body = TextAreaField(u'Body', validators=[validators.InputRequired()])
    userId = HiddenField('User', validators=[validators.InputRequired()])
    leagueId= HiddenField('League', validators=[validators.InputRequired()])
    index = HiddenField('Index', validators=[validators.InputRequired()])

    def validate_body(form, field):
        if len(field.data) > 1000:
            raise ValidationError("1000 character limit exceeded")