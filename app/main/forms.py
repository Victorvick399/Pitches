from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):

    title = StringField('Comments',validators=[Required()])
    review = TextAreaField('Pitch comment')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write your description here...',validators=[Required()])
    submit = SubmitField('Submit')