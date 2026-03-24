#apps.app으로부터 db를 import
from apps.app import db
# 작성한 SignUpForm 클래스  import
from apps.auth.forms import SignUpForm, LoginForm
# crud 앱의 모델의 User 클래스 import
from apps.models.user import User
# flash, url_for, redirect, request를 추가로 import
from flask import Blueprint, render_template, flash, url_for, redirect, request
# flask_login으로부터 login_user를 import. login_user 이용해서 등록한 사용자 정보 세션에 저장
from flask_login import login_user, logout_user
from sqlalchemy.exc import IntegrityError


# Blueprint 사용해서 auth 생성
auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@auth.route("/signup", methods=["GET","POST"])
def signup():
    # SignUpForm 인스턴스화하기
    form = SignUpForm()

    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            nickname=form.username.data,
            email = form.email.data,
        )
        user.password = form.password.data
        
        # 이메일 중복 체크하기
        if User.is_duplicate_email(form.email.data):
            flash("This email is already in use.")
            return redirect(url_for("auth.signup"))
        
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash("This email is already in use.")
            return redirect(url_for("auth.signup"))

        # 사용자 정보를 세션에 저장하기
        login_user(user)

        flash("Your account has been created successfully.")

        # GET 파라미터에 next 키 존재하고, 값이 없는 경우 사용자의 일람 페이지로 리다이렉트하기
        next_ = request.args.get("next")
        if next_ is None or not next_.startswith("/"):
            next_ = url_for("crud.users")

        return redirect(next_)

    return render_template("auth/signup.html", form=form)

@auth.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 이메일 주소로 데이터베이스에 사용자가 있는지 검사
        user = User.query.filter_by(email=form.email.data).first()

        # 사용자가 존재하고 비밀번호가 일치하면 로그인을 허가함
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for("crud.users"))
        

        flash("Invalid email or password.")
    return render_template("auth/login.html", form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))