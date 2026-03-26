from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[
            DataRequired("Title is required."),
            Length(max = 500, message = "Please enter up to 500 characters."),
            ],       
     )
    content = TextAreaField(
        "Content",
        validators=[
            DataRequired("Content is required.")
            ],
    )
    submit = SubmitField("Post")