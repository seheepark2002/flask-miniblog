# 이메일 형식 검증 라이브러리
from email_validator import validate_email, EmailNotValidError # email의 올바른 형식 여부 체크 위한 Email밸리데이톨
# flask 기본 기능 import
from flask import Blueprint, render_template, url_for, request, redirect, flash

#miniblog 기능 담당 Blueprint
#template_folder와 static_folder 지정해서 해당 blueprint 내부에서 템플릿, 스택틱 파일 사용 가능
miniblog = Blueprint(
    "miniblog", __name__, template_folder="templates", static_folder="static",
)

#메인페이지
@miniblog.route("/main", methods=["GET","POST"], endpoint="blog_main") 
def main():
    return render_template("main.html")

#사용자 블로그 페이지
#url로 전달된 id 값으로 특정 사용자 페이지 표시하기
@miniblog.route("/main/<id>", methods=["GET","POST"], endpoint="id_homepage") #임의로 id로 했지만 나중에 uuid로 바꿔야할둣
def user_homepage(id):
    return f"{id}'s homepage!"

#nickname 기반 사용자 블로그 페이지
#nickname 값을 템플릿으로 전달
@miniblog.route("/nickname/<nickname>")
def show_nickname(nickname):
    return render_template("user_miniblog.html", nickname=nickname)

#문의 페이지. 사용자에게 문의폼 제공
@miniblog.route("/contact")
def contact():
    return render_template("contact.html")

#문의 완료 페이지.
#POST 요청 시 form 데이터를 검증 -> flash 메세지 표시
@miniblog.route("/contact/complete", methods=["GET","POST"])
def contact_complete():
    #POST 요청일 때만 form 데이터 처리
    if request.method == "POST":

        #form 데이터 가져오기
        # username = request.form["id"]  #form속성 사용해서 폼의 값 취득
        email = request.form.get("email")
        message = request.form.get("message")

        #validation 상태 변수
        is_valid = True
        # if not id:    #id 입력 대신 user_id 자동 기능 넣기
        #     flash("id is required.")
        #     is_valid = False

        #이메일 입력 여부 확인
        if not email:
            flash("Email address is required.")
            is_valid = False
        else:
             #이메일 형식 검증
            try: 
                validate_email(email)
            except EmailNotValidError:
                flash("Please enter a valid email address.")
                is_valid = False

        #문의 내용 입력 여부 확인
        if not message:
            flash("Message is required.")
            is_valid = False

        #validarion 실패 시 다시 contact 페이지로 리다이렉트
        if not is_valid:
            return redirect(url_for("miniblog.contact"))
        
        #정상 처리 메세지
        flash("Thank you for contacting us.")

        #문의 완료 페이지로 리다이텍트
        return redirect(url_for("miniblog.contact_complete"))
    #GET 요청 시 완료 페이지 렌더링
    return render_template("contact_complete.html")