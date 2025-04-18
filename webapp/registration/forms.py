# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField, BooleanField, URLField, EmailField

# from wtforms.validators import DataRequired, Length

# class RegForm(FlaskForm):
#     label2 = StringField("Регистрация" )
#     email = EmailField("Почта:" , validators=[DataRequired()])
#     username1 = StringField("Имя пользователя:" , validators=[DataRequired()])
#     password_fir = PasswordField("Пароль: " , validators=[DataRequired(),  Length(min=2, max=20, message="Пароль должен содержать от 28 до 20 символов")])   # Ограничение на длину почты 8-20
#     password_sec = PasswordField("Подтвердите пароль: " , validators=[DataRequired(),  Length(min=2, max=20, message="Пароль должен содержать от 2 до 20 символов")])
#     submit_reg = SubmitField("Регистрация")
