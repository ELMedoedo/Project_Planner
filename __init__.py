from flask import Flask, render_template
from forms import LoginForm, PassRecForm, ChekMail
# from flask_login import Loginmanager

 
app = Flask(__name__)
app.config.from_pyfile("config.py")

@app.route("/")
def index():
    return render_template(
        "index.html"
    )

@app.route("/login")
def login():
    title = "Авторизация"
    login_form = LoginForm()
    return render_template(
        "login.html", page_title = title, form = login_form
    )


@app.route("/chekmail")
def chekmail():
    title = "Проверка Почты"
    chekmail_form = ChekMail()
    return render_template(
        "chekmail.html", page_title = title, form = chekmail_form
    )



@app.route("/passrec")
def passrec():
    title = "Восстановление пароля"
    passrec_form = PassRecForm()
    return render_template(
        "passrec.html", page_title = title, form = passrec_form
    )




if __name__ == "__main__":
    app.run(debug=True)