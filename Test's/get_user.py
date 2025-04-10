from sqlalchemy import select # Это аналог команды из SQL 

from database import db_session
from models import User


my_user = select(User) # внутрь select мы передаем модель, чтобы sqlalchemy знал, по какой таблице ему пройтись
my_user_res = db_session.execute(my_user) # Вызываем метод execute у db_se.. И в этот Экзекьбют нужно передать запрос
users = my_user_res.scalars()    #метод скаларс. Представляет соболй ответ от базы в виде класса питона, который мы ему предоставили. в данном случае в связи с модельной Юзер. Скаларс содержит все строчки. Скалар только 1

for user in users:
    print(f"""
    Зарплата: {user.user}
    Почта: {user.email}
""")