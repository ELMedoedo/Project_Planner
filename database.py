from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, scoped_session
from config import SQLALCHEMY_DATABASE_URI

engine=create_engine(SQLALCHEMY_DATABASE_URI)

db_session=scoped_session(sessionmaler(bind=engine))

db=SQLALchemy

class Basa(DeclarativeBase):
    pass
