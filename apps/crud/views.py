from flask import Blueprint, render_template
from apps.app import db
from apps.models.user import User

crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@crud.route("/")
def index():
    return render_template("crud/sign_in.html")

@crud.route("/sql")
def sql():
    users = db.session.query(User).all()
    return "콘솔 로그를 확인해주세요"