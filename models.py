from sqlalchemy import String, DateTime
from database import Base, engine
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
# from werkzeug.security import generate_password_hash, check_password_hash


class User(Base):
    __tablename__ = "users"  # Атрибут. название колонки
    id: Mapped[int] = mapped_column(primary_key=True) #Колонка с уникальным номером строки
    login: Mapped[str] = mapped_column(String(120))  # Логин пользователя, не больше 120 символов
    email: Mapped[str] = mapped_column(unique=True) # колонка с почтой пользователя, уникальные значения.
    password: Mapped[str] = mapped_column(String(40)) 
    city: Mapped[str] = mapped_column(nullable=True)
    birthday: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    # def set_password(self, password):
    #     self.password = generate_password_hash(password) # преобразование  Пассворд в зашифрованную строку. результат кладется в атрибут обьекта пассворд в данном случае

    # def check_password(self, password):
    #     return check_password_hash(self.password, password) # достаем зашифрованный пароль из базы данных (туда положил генератор его)б и пароль, пришедший от юзера. Зашифрует то, что пришло от пользователя и сверит. На выходе True либо False


    def __repr__(self): # метод класса, который отобразит читаемое отображание атрибутов
        return f"<User: {self.login}, {self.email}, Birthday: {self.birthday}>"

# для создания таблицы -  необходимо запустить сам файл models
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    #интепретатор обращается к Base, импортируемые из database, обращемся к метадате Base, в методате есть метод create_all - который создаст все таблицы. БЕЗ ЗАДВОЕНИЙ



