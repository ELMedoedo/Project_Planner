from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, URLField

from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    label1 = StringField("Вход" )
    label2 = StringField("Регистрация" )
    username_email = StringField("Имя пользователя или Почта:" , validators=[DataRequired()])
    username = StringField("Имя пользователя:" , validators=[DataRequired()])
    email = StringField("Почта:" , validators=[DataRequired()])
    password = PasswordField("Пароль: " , validators=[DataRequired(),  Length(min=8, max=20, message="Пароль должен содержать от 8 до 20 символов")])   # Ограничение на длину почты 8-20
    password_sec = PasswordField("Подтвердите пароль: " , validators=[DataRequired(),  Length(min=8, max=20, message="Пароль должен содержать от 8 до 20 символов")])
    # hidden_tag = HiddenField
    submit_in = SubmitField("Авторизация")
    submit_reg = SubmitField("Регистрация")
    save_login = BooleanField("Запомнить меня")
    forgot_pas = SubmitField("Пароль утерян?")

class ChekMail(FlaskForm):
    chek_email = StringField("!!Выводить результат!! Мэйл не найдет, либо выслано письмо. Так же кул даун на кнопку в 10 секунд" )
    start_chek_and_send = StringField("Восстановить" )


class PassRecForm(FlaskForm):
    chek_pass1 = StringField("!!ставить галочку при нахождении в лимите 8 -20 символов!!" )
    chek_pass2 = StringField("!!ставить галочку при одинакого введенном пароле с chek_pass1" )
    start_rec_pass = StringField("Обновить пароль" )