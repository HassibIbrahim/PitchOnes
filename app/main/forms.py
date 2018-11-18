from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required, DataRequired


class UpdateProfile(FlaskForm):
        bio = TextAreaField('Tell us about you.', validators=[DataRequired()])
        submit = SubmitField('Submit')
