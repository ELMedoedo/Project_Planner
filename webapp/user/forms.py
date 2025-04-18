from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, URLField, EmailField

from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField("Имя пользователя или Почта:" , validators=[DataRequired()], render_kw = {"class": "form-control"})
    password = PasswordField("Пароль:" , validators=[DataRequired()], render_kw = {"class": "form-control"})
    submit_in = SubmitField("Авторизация")
    save_login = BooleanField("Запомнить меня", default=True, render_kw={"class": "form-check-input"})
    forgot_pas = SubmitField("Пароль утерян?")


class ChekMail(FlaskForm):
    chek_email = StringField("!!Выводить результат!! Мэйл не найдет, либо выслано письмо. Так же кул даун на кнопку в 10 секунд" )
    start_chek_and_send = StringField("Восстановить" )


class PassRecForm(FlaskForm):
    password_fir = PasswordField("Пароль: " , validators=[DataRequired()], render_kw = {"class": "form-control"}) ,
    password_sec = PasswordField("Подтвердите пароль: " , validators=[DataRequired(), EqualTo(password_fir)], render_kw = {"class": "form-control"})
    chek_pass1 = StringField("!!ставить галочку при нахождении в лимите 8 -20 символов!!" )
    chek_pass2 = StringField("!!ставить галочку при одинакого введенном пароле с chek_pass1" )
    start_rec_pass = StringField("Обновить пароль" )


class RegForm(FlaskForm):
    label2 = StringField("Регистрация" )
    email = EmailField("Почта:" , validators=[DataRequired(), Email()], render_kw = {"class": "form-control"})
    username1 = StringField("Имя пользователя:" , validators=[DataRequired()], render_kw = {"class": "form-control"})
    password_fir = PasswordField("Пароль: " , validators=[DataRequired()], render_kw = {"class": "form-control"}) ,
    password_sec = PasswordField("Подтвердите пароль: " , validators=[DataRequired(), EqualTo(password_fir)], render_kw = {"class": "form-control"})
    submit_reg = SubmitField("Регистрация")
