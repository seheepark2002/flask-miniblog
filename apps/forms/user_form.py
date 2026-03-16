from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class UserForm(FlaskForm): #FlaskForm을 상속한 UserForm 클래스 작성 #사용자 생성 및 수정에 사용

    username = StringField(
        "Username",
        validators=[
            DataRequired(message="Username is required."),
            Length(max=30, message="Username must be 30 characters or fewer."),
        ]
    )

    email = StringField(
        "Email Address",
        validators=[
            DataRequired(message="Email is required."),
            Email(message="Please enter a valid email address."),
        ],
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Password is required."),
            Length(min=8, message="Password must be at least 8 characters long."),
            ]
    )

    submit = SubmitField("Create Account")