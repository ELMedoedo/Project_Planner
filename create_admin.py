from getpass import getpass # скрывание пароля из отоброжания (звездочки вместо пароля)
import sys  # модуль взаимодействия с системными вызовами
from webapp.models import User
from webapp.database import db
from webapp import create_app

app = create_app()  # Создаем экземпляр приложения
with app.app_context():  # Работаем в контексте приложения (для доступа к конфигурации и БД)
    username = input('Введите имя пользователя: ')

    if User.query.filter_by(user=username).first():  # Проверка существования пользователя через Flask-SQLAlchemy
        print('Такой пользователь уже есть')
        sys.exit(0)

    password1 = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')
    if not password1 == password2:
        print("Пароли не совпадают!")
        sys.exit(0)


    new_user = User(user = username, role = "admin")
    new_user.set_password(password2)

    db.session.add(new_user)
    db.session.commit()
    print("User: {}".format(new_user.id))
