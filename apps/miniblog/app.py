from email_validator import validate_email, EmailNotValidError # email의 올바른 형식 여부 체크 위한 Email밸리데이톨
from flask import Flask, render_template, url_for, request, redirect, current_app, flash

app = Flask(__name__)

app.config["SECRET_KEY"] = "83hfwkfn3SJW3"  #secret_key 추가
@app.route("/main", methods=["GET","POST"], endpoint="blog-main") # @app.route() 대신 @app.get("/hello") 가능
def main():
    return render_template("main.html")

@app.route("/main/<id>", methods=["GET","POST"], endpoint="id-homepage") #임의로 id로 했지만 나중에 uuid로 바꿔야할둣
def user_homepage(id):
    return f"{id}'s homepage!"

@app.route("/nickname/<nickname>")
def show_nickname(nickname):
    return render_template("user_miniblog.html", nickname=nickname)

# with app.test_request_context():
#     print(url_for("id-homepage", id="1234")) #나중에 uuid로 바꾸기
#     print(url_for("id-homepage"))
#     print(url_for("show_nickname", nickname="닉네임"))


# ctx = app.app_context()
# ctx.push()

# print(current_app.nickname)

# g.connection = "connection"
# print(g.connection)

# with app.test_request_context("/users?updated=true"):
#     print(request.args.get("updated"))


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods=["GET","POST"])
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
            flash("email address is required.")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("Please enter a valid email address.")
            is_valid = False

        if not message:
            flash("Message is required.")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))
        
        flash("Thank you for contacting us.")

        return redirect(url_for("contact_complete"))
    
    return render_template("contact_complete.html")