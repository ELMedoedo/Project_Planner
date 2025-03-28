from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
engine=create_engine(SQLALCHEMY_DATABASE_URI)

db_session=scoped_session(sessionmaker(bind=engine))

db=SQLAlchemy(app)

class Base(db.Model):
    __abstract__ = True

