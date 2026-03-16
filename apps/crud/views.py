from flask import Blueprint, render_template, redirect, url_for, flash, request
from apps.app import db
from apps.models.user import User
from apps.forms.user_form import UserForm

# Blueprint 생성
#url_for 에서 "crud.route_name" 형태로 사용
crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)
 #기본 페이지(로그인 페이지)
@crud.route("/")
def index():
    return render_template("crud/sign_in.html")

# sql테스트용 #sql 로그 콘솔 출력 확인용 페이지
@crud.route("/sql") 
def sql():
    users = db.session.query(User).all()
    return "콘솔 로그를 확인해주세요"

#사용자 신규 등록 페이지 #GET -> 사용자 등록 form 표시 
# #POST -> form validation 후 DB에 사용자 저장 
@crud.route("/users/new", methods=["GET","POST"])
def create_user():

    #Flask-WTF form 객체 생성
    form = UserForm()

    #POST 요청, validation 성공한 경우
    if form.validate_on_submit():

        #User 모델 인스턴스 생성
        user = User(
            username=form.username.data,
            nickname=form.username.data,
            email=form.email.data,
        )
        #password property 통해서 비번 자동으로 hash로 저장
        user.password=form.password.data

        # DB 세션에 추가 후 commit
        db.session.add(user)
        db.session.commit()

        #등록 완료 메세지
        flash("User has been created successfully.")
        #사용자 목록 페이지로 리다이렉트
        return redirect(url_for("crud.users"))
    #GET 요청이면 사용자 등록 페이지 표시
    return render_template("crud/create_user.html", form=form)

#사용자 목록 페이지
#DB에 저장된 사용자 데이터 조회, users.html로 전달
@crud.route("/users")
def users():
    users = db.session.query(User).all()
    return render_template("crud/users.html", users=users)

#사용자 수정 페이지
#url에 전달된 user_id로 사용자 조회 후 수정
@crud.route("/users/<user_id>/edit", methods=["GET","POST"])
def edit_user(user_id):
    form = UserForm()

    #
    user = User.query.get_or_404(user_id)

    #사용자 존재하지 않는 경우 목록페이지로 리다이렉트
    if user is None:
        flash("User not found.")
        return redirect(url_for("crud.users"))

    #GET요청 시 기존 사용자 정보를 form에 채워 넣음
    if request.method == "GET":
        form.username.data = user.username
        form.email.data = user.email

    #POST 요청 시 form validation 후 DB 업데이트
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))
    
    return render_template("crud/edit_user.html", user=user, form=form)