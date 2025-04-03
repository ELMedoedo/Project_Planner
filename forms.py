from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, URLField

from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    label1 = StringField("Вход" )
    label2 = StringField("Регистрация" )
    username_email = StringField("Имя пользователя или Почта:" , validators=[DataRequired()])
    username = StringField("Имя пользователя:" , validators=[DataRequired()])
    email = StringField("Почта:" , validators=[DataRequired()])
    password = PasswordField("Пароль: " , validators=[DataRequired()])
    password_sec = PasswordField("Подтвердите пароль: " , validators=[DataRequired()])
    # hidden_tag = HiddenField
    submit_in = SubmitField("Авторизация")
    submit_reg = SubmitField("Регистрация")
    save_login = BooleanField("Запомнить меня")
    forgot_pas = SubmitField("Пароль утерян?")





