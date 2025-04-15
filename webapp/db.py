
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Base(db.Model): 
    __abstract__ = True #  класс абстрактный

