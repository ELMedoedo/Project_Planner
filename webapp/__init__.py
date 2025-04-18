from flask import Flask, render_template, flash, redirect, url_for
from webapp.database import db
from webapp.forms import LoginForm, RegForm, PassRecForm, ChekMail
from flask_login import LoginManager, login_user, logout_user
from webapp.models import User


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


    @app.route("/")
    def index():
        return render_template("index.html")


    @app.route("/login")
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        reg_form = RegForm()
        return render_template(
            "login.html", page_title=title, login_form=login_form, reg_form=reg_form
        )


    @app.route("/process-login", methods=["POST"])
    def process_login():
        form = LoginForm()  # создаем форму

        if (
            form.validate_on_submit()
        ):  # Если данные формы пришли и она валидируется. Если возникнут ошибки (пользователь не заполнил поля).
            user = User.query.filter(
                User.user == form.username.data
            ).first()  # запрашиваем пользователя из базы данных (в форме данные лежат в Формс)
            if user and user.check_password(
                form.password.data
            ):  # если такой пользователь есть, то при помощи инструмента (функционал проверки пароля)
                login_user(user)
                flash("Вы успешно вошли на сайт!")
                return redirect(url_for("index"))
            
            # else:
            #     flash("Мда!")
            #     return redirect(url_for("index"))


        flash("Не правильное имя или пароль")
        return redirect(url_for("login"))


    @app.route("/chekmail")
    def chekmail():
        title = "Проверка Почты"
        chekmail_form = ChekMail()
        return render_template("chekmail.html", page_title=title, form=chekmail_form)


    @app.route("/passrec")
    def passrec():
        title = "Восстановление пароля"
        passrec_form = PassRecForm()
        return render_template("passrec.html", page_title=title, form=passrec_form)


    @app.route("/logout")
    def logout():
        logout_user()
        flash("Вы вышли из системы")
        return redirect(url_for("login"))

    return app
