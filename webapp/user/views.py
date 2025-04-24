from flask import  Blueprint, render_template, flash, redirect, url_for
# from webapp.registration.forms import RegForm
from webapp.user.forms import LoginForm, ChekMail, PassRecForm, RegForm
from webapp.user.models import User
from flask_login import  login_user, current_user, login_required
from webapp.db import db

blueprint = Blueprint("user", __name__, url_prefix="/user")


@blueprint.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("planner.planner"))
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
            return redirect(url_for("planner.planner"))
        

        flash("Не правильное имя или пароль")
        return redirect(url_for("user.login"))

@blueprint.route("/process_registration", methods=["POST"])
def process_registration():
    form = RegForm()

    if form.validate_on_submit():
        # Проверка на существующее имя пользователя
        existing_user = User.query.filter(
            User.user == form.username1.data  
        ).first()
        
        # Проверка на существующий email
        existing_email = User.query.filter(
            User.email == form.email.data  
        ).first()

        if existing_user:
            flash("Этот логин уже занят")
            return redirect(url_for("user.login"))  # Перенаправляем обратно на страницу регистрации

        if existing_email:
            flash("Эта почта уже зарегистрирована")
            return redirect(url_for("user.login"))

        new_user = User(
            user=form.username1.data,
            email=form.email.data,
            role = "user"
        )
        new_user.set_password(form.password_fir.data)
        db.session.add(new_user)
        db.session.commit()
        
        flash("Регистрация прошла успешно!")
        return redirect(url_for("user.login"))
    
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"Ошибка в поле '{getattr(form, field).label.text}': {error}")
    return redirect(url_for("user.login") + "#collapseTwo") 

        
        

@blueprint.route("/chekmail")
def chekmail():
    title = "Проверка Почты"
    chekmail_form = ChekMail()
    return render_template("login/chekmail.html", page_title=title, form=chekmail_form)


@blueprint.route("/passrec")
def passrec():
    title = "Восстановление пароля"
    passrec_form = PassRecForm()
    return render_template("login/passrec.html", page_title=title, form=passrec_form)

