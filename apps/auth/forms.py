from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignUpForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired("Username is required."),
            Length(min=1, max=30, message="Please enter up to 30 characters."),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired("Email is required."),
            Email("Please enter a valid email address."),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired("Password is required."),
            Length(min=8,message="Password must be at least 8 characters long."),
        ],
    )
    submit = SubmitField(
        "Create Account"
    )