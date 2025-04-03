from flask import request, jsonify
from database import db
from __init__ import app
from models import User
from werkzeug.security import generate_password_hash

@app.route('/create_user', methods=['POST'])
def create_user():

    data=request.get_json()


    # Проверка обязательных полей
    required_fields = {"email", "username", "password", "password_sec"} 
    if not data or not required_fields.issubset(data):
        return jsonify({"error": "Missing required fields"}), 400 # 400 — ошибка в данных от клиента

    # Проверка совпадения паролей
    if data["password"] != data["password_sec"]:
        return jsonify({"error": "Passwords do not match"}), 409 # 409 — конфликт (дубликат)

    # Проверка уникальности email и username. User.query - Это доступ к таблице users через SQLAlchemy. User —  модель (класс), а .query — инструмент для построения SQL-запросов.
    if User.query.filter_by(email=data["email"]).first():  #обращаемся к таблице, к отфильтрованной колонке email. При возникновении совпадения - Ошибка
        return jsonify({"error": "Email already exists"})
    if User.query.filter_by(username=data["username"]).first():  # Аналогично обращаемся к колонке username. 
        return jsonify({"error": "Username already exists"}), 409
    try:
        new_user=User(
            username = data["username_email"],
            email = data["email"],
            password_hash=generate_password_hash(data["password"])  # Пароль хешируется. Пароли уже точно одинаковые. сразу его шифруем.

        )

        # db — это центральный объект SQLAlchemy, созданный при старте приложения.
        db.session.add(new_user)   # Готовим данные к сохранению. Добавляем объект new_user (созданный экземпляр класса User) в текущую сессию.
        db.session.commit()  # Фиксируем все изменения в базе данных. появился новый пользователь в таблице users

        return jsonify({'message':'User was created successfully', 'task':{
            "id": new_user.id,
            "email": new_user.email ,
            "username": new_user.username,
        }})
    except Exception as err: # ловим любую ошибку, любое исключение, которое возникло в блоке try. Exception - базовый класс всех ошибок. еrr - переменная, содерж. инф об ошибке
        db.session.rollback()  # Откатывает все несохранённые изменения в текущей сессии работы с БД. Не оставляем базу в подвешенном состоянии
        return jsonify({"error": "Internal server error"}), 500 # Возвращаем JSON-ответ с сообщением об ошибке и HTTP-статусом 500
    
    # Но, возвращать str(err) - нельзя, т.к. она хранит информацию о бд. МОжет хранить прочую важную инфу.