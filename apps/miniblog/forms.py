from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

# 문의폼 
class ContactForm(FlaskForm):
    # 이메일 입력
    email = StringField(
        "email",
        validators=[
            DataRequired("Email is required."),
            Email("Please enter a valid email address."),
        ],
    )
    # 메세지 입력
    message = StringField(
        "Message",
        validators=[
            DataRequired("Message is required.")
        ],
    )
    #보내기 버튼 
    submit = SubmitField("Send")