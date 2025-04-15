from sqlalchemy import select

from webapp.database import db
from webapp.models import User

def top_user(row_num):
    top_users = select(User).order_by(User.user.desc()).limit(row_num)     # desc - тип сортировки от большего к меньшему. asc - от меньшего к большему. limit - какой нам нужен срез от выборки
    top_users_res = db.session.execute(top_users).scalars()
    for user in top_users_res:
        print(f"Пользователь по алвафитному порядку: {user.user}")


def top_email(domain_name, row_st):
    top_email = select(User).order_by(User.email.like(f"% { domain_name } %"))\
                    .order_by(User.email.desc()).limit(row_st)  # проверка вхождения в строку, методом like() от СКЛАлхимии. %% - означает, что до и после этой подстроки (Кот мы ищем) могут стоять любые символы
    top_email_res = db.session.execute(top_email).scalars()
    print(domain_name)
    for us in top_email_res:
        print(f"Name: {us.user}")

    

if __name__ == "__main__":
    # top_user(4) # переменная, которая указывает, сколько значений нам возвращать
    top_email("@4", 3)   # 3 - лимит (в конце функции) 