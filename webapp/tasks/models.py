from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date, datetime
from sqlalchemy import Enum

from webapp.db import db  
from webapp.static.enums import ActionType, ObjectType


class Dashboard(db.Model):
    __tablename__ = "dashboards"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'))
    user_name: Mapped[str] = mapped_column(db.String(120))
    table_type: Mapped[str] = mapped_column(db.String(50), nullable=True)
    table_comment: Mapped[str] = mapped_column(db.Text, nullable=True)
    tasks: Mapped[list["Task"]] = relationship('Task', back_populates='dashboard', cascade='all, delete-orphan')
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self):
        return f"<Board: {self.user_id}, {self.table_type}, Comment: {self.table_comment}>"


class Task(db.Model):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    dashboard_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('dashboards.id'))
    title: Mapped[str] = mapped_column(db.String(100), nullable=False)
    body: Mapped[str] = mapped_column(db.Text, nullable=False)
    status: Mapped[str] = mapped_column(db.String(50))
    due_date: Mapped[date] = mapped_column(db.Date, nullable=False)
    dashboard: Mapped["Dashboard"] = relationship('Dashboard', back_populates='tasks')  

    def __repr__(self):
        return f"<Tasks {self.title}: {self.body}, Status: {self.status}>"


class Task_SubPlan(db.Model):
    __tablename__ = "task_subplans"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    task_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('tasks.id'))
    title: Mapped[str] = mapped_column(db.String(100), nullable=True)
    body: Mapped[str] = mapped_column(db.Text, nullable=True)
    status: Mapped[str] = mapped_column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<SubPlan {self.title}: {self.body}, Status: {self.status}>"


class Planer_History(db.Model):
    __tablename__ = "plan_history"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)  
    user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'))  
    action: Mapped[ActionType] = mapped_column(Enum(ActionType))
    object_type: Mapped[ObjectType] = mapped_column(Enum(ObjectType))
    object_id: Mapped[int] = mapped_column(db.Integer)  # ID связанного объекта
    details: Mapped[str] = mapped_column(db.String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self):
        return f"<Action: {self.action.value} {self.object_type.value}, Time: {self.created_at}>"