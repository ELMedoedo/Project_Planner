from database import db_session 
from models import User

first_user = User(user = "Bust5", email = "buSest5@4.ru", password = "1")
db_session.add(first_user)   # Сформировываем запрос. Для добавления пользователя Вызываем у обьекта ДБ_сес вызвать метод Эдд. 
db_session.commit() # метод накатывает изменения на нашу базу. 