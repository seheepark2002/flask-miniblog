from apps.miniblog.forms import ContactForm
from flask import Blueprint, render_template, flash

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
@miniblog.route("/contact", methods = {"GET", "POST"})
def contact():
    form = ContactForm()

    if form.validate_on_submit():
            email = form.email.data
            message = form.message.data

            flash("Thank you for contacting us.")
            return render_template("contact_complete.html")

    return render_template("contact.html", form = form)


        
    