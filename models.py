from sqlalchemy import String, DateTime, ForeignKey, Date
from flask_login import UserMixin
from database import Base, engine
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base):    # , UserMixin
    __tablename__ = "users"  # Атрибут. название колонки
    id: Mapped[int] = mapped_column(primary_key=True) #Колонка с уникальным номером строки
    user: Mapped[str] = mapped_column(String(120))  # Логин пользователя, не больше 120 символов
    email: Mapped[str] = mapped_column(unique=True) # колонка с почтой пользователя, уникальные значения.
    password: Mapped[str] = mapped_column(String(40)) 
    city: Mapped[str] 
    birthday: Mapped[Date] = mapped_column(Date)

    def set_password(self, password):
        self.password = generate_password_hash(password) # преобразование  Пассворд в зашифрованную строку. результат кладется в атрибут обьекта пассворд в данном случае

    def check_password(self, password):
        return check_password_hash(self.password, password) # достаем зашифрованный пароль из базы данных (туда положил генератор его)б и пароль, пришедший от юзера. Зашифрует то, что пришло от пользователя и сверит. На выходе True либо False


    def __repr__(self): # метод класса, который отобразит читаемое отображание атрибутов
        return f"<User: {self.user}, {self.email}, Birthday: {self.birthday}>"
    

class Dashboard(Base):
    __tablename__ = "dashboards"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id), index=True)
    user_name: Mapped[str] 
    table_type: Mapped[str] 
    table_comment: Mapped[str]

    def __repr__(self): # метод класса, который отобразит читаемое отображание атрибутов
        return f"<Board: {self.user_id}, {self.table_type}, Comment: {self.table_comment}>"

class Task(Base):
    __tablename__="Tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    table_id: Mapped[int] = mapped_column(ForeignKey(Dashboard.id), index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    body: Mapped[str]
    status: Mapped[str] =  mapped_column(String(50), nullable=False, default="Новая")

    def __repr__(self):
        return f"<Tasks {self.title}: {self.body}, Status: {self.status}>"

class Task_SubPlan(Base):
    __tablename__ = "Task_SubPlans"
    i: Mapped[int] = mapped_column(primary_key=True)
    table_id: Mapped[int] = mapped_column(ForeignKey(Task.id), index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=True)
    body: Mapped[str] 
    status: Mapped[str] =  mapped_column(String(50), nullable=False)

    def __repr__(self):
        return f"<SubPlan {self.title}: {self.body}, Status: {self.status}>"

# для создания таблицы -  необходимо запустить сам файл models
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    #интепретатор обращается к Base, импортируемые из database, обращемся к метадате Base, в методате есть метод create_all - который создаст все таблицы. БЕЗ ЗАДВОЕНИЙ



