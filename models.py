from sqlalchemy import String, DateTime, Text, Integer, Column
from sqlalchemy.orm import Mapped, mapped_column
from database import Base, engine, db
from datetime import datetime

class Tasks(Base):
    __tablename__='Tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="новая")

    def __repr__(self):
        return f'<Tasks {self.title}: {self.body}, Status: {self.status}>'

if __name__=='__main__':
    Base.metadata.create_all(bind=engine)



