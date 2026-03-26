# Flask 웹 기능 import  
from flask import Blueprint, render_template, redirect, url_for, flash
# apps/app.py에서 DB객체 가져오기
from apps.app import db
# 로그인 필수 import
from flask_login import login_required, current_user
# post 모델 클래스 가져오기
from apps.models.post import Post
# PostForm 클래스 가져오기
from apps.posts.forms import PostForm

# Blueprint 객체 생성하기
posts = Blueprint(
    "posts",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# 글 목록 페이지 경로 만들기
@posts.route("/")
def list_posts():
    # 최신 글부터 보이기
    posts_list = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("posts/posts.html", posts = posts_list)

# 글쓰기 페이지 경로 만들기 메소드="GET","POST"
@posts.route("/new", methods = ["GET", "POST"])
# 로그인 필수
@login_required
# PostForm 클래스로 form 객체 만들기
def create_post():
    form = PostForm()
    # 조건문으로 폼이 "POST" 방식으로 제츨되고, 입력값이 유효한지 검증하기
    if form.validate_on_submit():

        # 입력값으로 Post 모델 객체 생성
        post = Post(
            title = form.title.data,
            content = form.content.data,
            # 작성자랑 작성자 글 연결하기
            user_id = current_user.id
        )

        # db에 저장
        db.session.add(post)
        db.session.commit()

        # 글 게시 성공 안내 문구 띄우기
        flash("Post created successfully.")
        # 글 목록으로 리다이렉트
        return redirect(url_for("posts.list_posts"))
    
    return render_template("posts/create_post.html", form = form)
