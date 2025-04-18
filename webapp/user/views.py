from flask import  Blueprint, render_template, flash, redirect, url_for
# from webapp.registration.forms import RegForm
from webapp.user.forms import LoginForm, ChekMail, PassRecForm, RegForm
from webapp.user.models import User
from flask_login import  login_user, logout_user

blueprint = Blueprint("user", __name__, url_prefix="/users")


@blueprint.route("/login")
def login():
    title = "Авторизация"
    login_form = LoginForm()
    reg_form = RegForm()
    return render_template(
        "login/login.html", page_title=title, login_form=login_form, reg_form=reg_form
    )

@blueprint.route("/process-login", methods=["POST"])
def process_login():
    form = LoginForm() 

    if (
        form.validate_on_submit()
    ): 
        user = User.query.filter(
            User.user == form.username.data
        ).first()  
        if user and user.check_password(
            form.password.data
        ): 
            login_user(user, remember=form.save_login.data)
            flash("Вы успешно вошли на сайт!")
            return redirect(url_for("task.planner"))
        

        flash("Не правильное имя или пароль")
        return redirect(url_for("user.login"))


@blueprint.route("/chekmail")
def chekmail():
    title = "Проверка Почты"
    chekmail_form = ChekMail()
    return render_template("user/chekmail.html", page_title=title, form=chekmail_form)


@blueprint.route("/passrec")
def passrec():
    title = "Восстановление пароля"
    passrec_form = PassRecForm()
    return render_template("user/passrec.html", page_title=title, form=passrec_form)

