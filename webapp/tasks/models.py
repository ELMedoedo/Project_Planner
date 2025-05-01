from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from webapp.db import db  



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
    dashboard_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('dashboards.id'))
    title: Mapped[str] = mapped_column(db.String(100), nullable=False)
    body: Mapped[str] = mapped_column(db.Text, nullable=False)
    status: Mapped[str] = mapped_column(db.String(50), default="Новая")
    due_date: Mapped[date] = mapped_column(db.Date, nullable=False)
    # due_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

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
    