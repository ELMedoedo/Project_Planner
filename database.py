from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase    #orm - модуль библиотеки. scoped_session - несколько сессий в рамках одного 1 подключения. Sessionmaker - создает сессию. классс Declarativebase - заимствуем из алхимии уже готовые методы для работы с базой (к примеру - создание табличек).
from config1 import SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy


engine = create_engine(SQLALCHEMY_DATABASE_URI)   #движок с параметрами подключения
db_session = scoped_session(sessionmaker(bind=engine))
db=SQLAlchemy()

class Base(DeclarativeBase): # кастомный , который наследуем от импортированного DeclarativeBase.
    pass 
