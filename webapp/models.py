from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from webapp.database import db  
from sqlalchemy.orm import Mapped, mapped_column


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    role: Mapped[str] = mapped_column(db.String(50))
    user: Mapped[str] = mapped_column(db.String(120), unique=True)
    email: Mapped[str] = mapped_column(db.String(120), unique=True, nullable=True)
    password: Mapped[str] = mapped_column(db.String(256))
    city: Mapped[str] = mapped_column(db.String(100), nullable=True)
    birthday: Mapped[str] = mapped_column(db.Date, nullable=True)


    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User: {self.user}, {self.email}, Роль: {self.role}>"


class Dashboard(db.Model):
    __tablename__ = "dashboards"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'))
    user_name: Mapped[str] = mapped_column(db.String(120))
    table_type: Mapped[str] = mapped_column(db.String(50), nullable=True)
    table_comment: Mapped[str] = mapped_column(db.Text, nullable=True)


    def __repr__(self):
        return f"<Board: {self.user_id}, {self.table_type}, Comment: {self.table_comment}>"


class Task(db.Model):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    table_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('dashboards.id'))
    title: Mapped[str] = mapped_column(db.String(100), nullable=True)
    body: Mapped[str] = mapped_column(db.Text, nullable=True)
    status: Mapped[str] = mapped_column(db.String(50), default="Новая")

    def __repr__(self):
        return f"<Tasks {self.title}: {self.body}, Status: {self.status}>"


class Task_SubPlan(db.Model):
    __tablename__ = "task_subplans"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    task_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('tasks.id'), nullable=True )
    title: Mapped[str] = mapped_column(db.String(100), nullable=True)
    body: Mapped[str] = mapped_column(db.Text, nullable=True)
    status: Mapped[str] = mapped_column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<SubPlan {self.title}: {self.body}, Status: {self.status}>"
    