from flask import request, jsonify
from database import db
from __init__ import app
from models import User
from werkzeug.security import generate_password_hash


@app.route("/create_user", methods=["POST"])
def create_user():


    # request.get_json() - Извлекает JSON-данные из тела (body) HTTP-запроса. Преобразует их в словарь Python (или список, если JSON был массивом). Инструмент Flask
    data = request.get_json()

    # Проверка обязательных полей
    required_fields = {"email", "username", "password", "password_sec"} # множество обязательных полей
    if not data or not required_fields.issubset(data):   #Метод issubset определяет, является ли одно множество подмножеством другого. Т.е. проверяет, все ли элементы `required_fields` присутствуют в ключах словаря `data`. Если хотя бы одно поле отсутствует, `issubset()` вернет `False`, а с оператором `not` это становится `True`, что приводит к выполнению условия.
        return (
            jsonify({"error": "Missing required fields"}),
            400,
        )  # 400 — ошибка в данных от клиента, данные обязательные- все должно быть введено

    # Проверка совпадения паролей
    if data["password"] != data["password_sec"]:
        return (
            jsonify({"error": "Passwords do not match"}),
            400,
        )  # 400 — конфликт (дубликат)
    
    if len(data["password"]) < 8 or len(data["password"]) > 20:
        return jsonify({"error": "Password must be at least 8 - 20 characters"}), 400

    # Проверка уникальности email и username. User.query - Это доступ к таблице users через SQLAlchemy. User —  модель (класс), а .query — инструмент для построения SQL-запросов.
    if User.query.filter_by(
        email = data["email"]
    ).first():  # обращаемся к таблице, к отфильтрованной колонке email. При возникновении совпадения - Ошибка
        return jsonify({"error": "Email already exists"}), 400
    if User.query.filter_by(
        username = data["username"]
    ).first():  # Аналогично обращаемся к колонке username.
        return jsonify({"error": "Username already exists"}), 400
    try:
        new_user = User(
            username = data["username"],
            email = data["email"],
            password_hash = generate_password_hash(
                data["password"]
            ),  # Пароль хешируется. Пароли уже точно одинаковые. сразу его и шифруем.
        )

        # db — это центральный объект SQLAlchemy, созданный при старте приложения.
        db.session.add(
            new_user
        )  # Готовим данные к сохранению. Добавляем объект new_user (созданный экземпляр класса User) в текущую сессию.
        db.session.commit()  # Фиксируем все изменения в базе данных. появился новый пользователь в таблице users

        return jsonify(
            {
                "message": "User was created successfully",
                "user": {
                    "id": new_user.id,
                    "email": new_user.email,
                    "username": new_user.username
                },
            }
        )
    except (
        Exception
    ):  # ловим любую ошибку, любое исключение, которое возникло в блоке try. Exception - базовый класс всех ошибок. еrr - переменная, содерж. инф об ошибке
        db.session.rollback()  # Откатывает все несохранённые изменения в текущей сессии работы с БД. Не оставляем базу в подвешенном состоянии
        return (
            jsonify({"error": "Internal server error"}),
            500,
        )  # Возвращаем JSON-ответ с сообщением об ошибке и HTTP-статусом 500

    # Но, возвращать str(err) - нельзя, т.к. она хранит информацию о бд. МОжет хранить прочую важную инфу.
    # Так что ее можно убрать в проде



#Проверяем почту в ДБ
@app.route("/chek_email", methods=["POST"])
def chek_email():

    data = request.get_json() #Получаем данные из запроса, преобразовываем в словарь.

    if not data : #1 - проверка на то, есть ли вообще данные в запросе
        return jsonify({"error": "Пустое поле"}), 400
    
    if "@" not in data["email"] or "." not in data["email"]: # проверка на корректность введения почты.
        return jsonify({"error": "Не верный формат почты"}), 400
    
    try:
        email_map = User.query.filter_by(email = data["email"]).first()
        # .query - метод для создания заросов к таблице (часть SQLAlchemy.orm)
        # .filter_by() (можно и filter, но он более долгий) фильтруем записи по колонке email
        # email = data["email"] - условие, где строка в столбце email равна значению data["email"]
        # .first() метод возвращает обьект таблицы User, если запись найдена, None - если не найдено. 

        if email_map:
            return jsonify({
                "exists" : True, # в JSON ответе - означает, что Мэйл уже есть в БД
                "message": "Email already registered"
            }), 200
        
        else:
            return jsonify({
                "exists": False, # в БД не найдено
                "message": "Email is available"
            }), 200
    except Exception:(
            jsonify({"error": "Internal server error"}),
            500,
        ) 

#Заносим пароль в БД 
@app.route("/pass_rec", methods=["POST"])
def pass_rec():

    data = request.get_json()

    required_fields = {"email", "pass1", "pass2"} 
    if not data or not required_fields.issubset(data):   # Проверяем, что Пароли введены оба
        return (
            jsonify({"error": "Missing required fields"}),
            400,
        )
    
    if data["pass1"] != data["pass2"]: # Проверка на одинаковые пароли
        return (
            jsonify({"error": "Passwords do not match"}),
            400,
        )  # 400 — конфликт (дубликат)
    
    if len(data["pass1"]) < 8 or len(data["password"]) > 20:
        return jsonify({"error": "Password must be at least 8 - 20 characters"}), 400
    
    try:   
        user_map = User.query.filter_by(email=data["email"]).first()      # Ищем пользователя по email
        
        if not user_map:
            return jsonify({"error": "User not found"}), 404
        # 404 - если пользователь не найден
        
                
        user_map.password_hash = generate_password_hash(data["pass1"])   # Обновляем пароль (хешируем новый пароль)
        db.session.commit()   # Фиксируем все изменения в базе данных. появился новый пользователь в таблице users

        return jsonify({
            "message": "Password updated successfully",
            "email": user_map.email
        }), 200
    

    except Exception:
        db.session.rollback()    # Откатывает все несохранённые изменения в текущей сессии работы с БД. Не оставляем базу в подвешенном состоянии!
        return jsonify({"error": "Internal server error"}), 500