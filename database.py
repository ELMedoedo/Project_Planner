from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase    #orm - модуль библиотеки. scoped_session - несколько сессий в рамках одного 1 подключения. Sessionmaker - создает сессию. классс Declarativebase - заимствуем из алхимии уже готовые методы для работы с базой (к примеру - создание табличек).
from config import SQLALCHEMY_DATABASE_URI


engine = create_engine(SQLALCHEMY_DATABASE_URI)   #движок с параметрами подключения
db_session = scoped_session(sessionmaker(bind=engine))

class Base(DeclarativeBase): # кастомный , который наследуем от импортированного DeclarativeBase.
    pass 
