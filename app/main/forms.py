from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import Required, DataRequired, Length, Email, ValidationError
from app.models import User
from flask_login import current_user


class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    description = TextAreaField(
        "What would you like to pitch ?", validators=[Required()])
    category = RadioField('Label', choices=[('promotionpitch', 'promotionpitch'), ('interviewpitch', 'interviewpitch'), (
        'pickuplines', 'pickuplines'), ('productpitch', 'productpitch')], validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):

    title = StringField('Comments', validators=[Required()])
    review = TextAreaField('Pitch comment')
    submit = SubmitField('Submit')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'That email is taken. Please choose a different one.')
