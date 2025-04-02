from sqlalchemy import String, DateTime
from database import Base, engine
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"  # Атрибут. название колонки
    id: Mapped[int] = mapped_column(primary_key=True) #Колонка с уникальным номером строки
    login: Mapped[str] = mapped_column(String(120))  # Логин пользователя, не больше 120 символов
    email: Mapped[str] = mapped_column(unique=True) # колонка с почтой пользователя, уникальные значения.
    password: Mapped[str] = mapped_column(String) # так же необходимо придумать, как шифровать пароли. Как вариант, отправлять их в функцию, где происходит шифр и тут выводить уже результат. Достаточно для начала просто шестнадцатиричного представлерия.
    city: Mapped[str] = mapped_column(String, nullable=True)
    birthday: Mapped[datetime] = mapped_column(DateTime, nullable=True)




    def __repr__(self): # метод класса, который отобразит читаемое отображание атрибутов
        return f"<User: {self.login}, {self.email}, Birthday: {self.birthday}>"

# для создания таблицы -  необходимо запустить сам файл models
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    #интепретатор обращается к Base, импортируемые из database, обращемся к метадате Base, в методате есть метод create_all - который создаст все таблицы. БЕЗ ЗАДВОЕНИЙ


# class Users(Base):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     login = db.Column(db.String(255), nullable=False)
#     email = db.Column(db.String(255), nullable=False)
#     password = db.Column(
#         db.String(255), nullable=False
#     )  # так же необходимо придумать, как шифровать пароли. Как вариант, отправлять их в функцию, где происходит шифр и тут выводить уже результат. Достаточно для начала просто шестнадцатиричного представлерия.
#     name = db.Column(db.String(255), nullable=True)
#     secondname = db.Column(db.String(255), nullable=True)
#     city = db.Column(db.String(255), nullable=True)
#     birthday = db.Column(db.datetime, nullable=True)


# if __name__ == "__main__":
#     Base.metadata.create_all(bind=engine)
