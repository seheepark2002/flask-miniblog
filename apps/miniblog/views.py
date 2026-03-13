from email_validator import validate_email, EmailNotValidError # email의 올바른 형식 여부 체크 위한 Email밸리데이톨
from flask import Blueprint, render_template, url_for, request, redirect, flash

miniblog = Blueprint(
    "miniblog", __name__, template_folder="templates", static_folder="static",
)

@miniblog.route("/main", methods=["GET","POST"], endpoint="blog_main") 
def main():
    return render_template("main.html")

@miniblog.route("/main/<id>", methods=["GET","POST"], endpoint="id_homepage") #임의로 id로 했지만 나중에 uuid로 바꿔야할둣
def user_homepage(id):
    return f"{id}'s homepage!"

@miniblog.route("/nickname/<nickname>")
def show_nickname(nickname):
    return render_template("user_miniblog.html", nickname=nickname)


@miniblog.route("/contact")
def contact():
    return render_template("contact.html")

@miniblog.route("/contact/complete", methods=["GET","POST"])
def contact_complete():
    if request.method == "POST":

        # username = request.form["id"]  #form속성 사용해서 폼의 값 취득
        email = request.form.get("email")
        message = request.form.get("message")

        is_valid = True
        # if not id:    #id 입력 대신 user_id 자동 기능 넣기
        #     flash("id is required.")
        #     is_valid = False

        if not email:
            flash("Email address is required.")
            is_valid = False
        else:
            try:
                validate_email(email)
            except EmailNotValidError:
                flash("Please enter a valid email address.")
                is_valid = False

        if not message:
            flash("Message is required.")
            is_valid = False

        if not is_valid:
            return redirect(url_for("miniblog.contact"))
        
        flash("Thank you for contacting us.")

        return redirect(url_for("miniblog.contact_complete"))
    
    return render_template("contact_complete.html")