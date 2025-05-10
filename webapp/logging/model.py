# from enum import Enum as PyEnum
# from webapp.db import db  
# from sqlalchemy.orm import Mapped, mapped_column
# from sqlalchemy import Enum
# from datetime import datetime




# class ActionType(PyEnum):
#     CREATE = "create"
#     DELETE = "delete"
#     UPDATE = "update"
    
# class ObjectType(PyEnum):
#     DASHBOARD = "dashbord"
#     Task = "task"

    
# class Planer_History(db.Model):
#     __tablename__ = "plan_history"
#     id: Mapped[int] = mapped_column(db.Integer, primary_key=True)  
#     user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'))  
#     action: Mapped[ActionType] = mapped_column(Enum(ActionType))
#     object_type: Mapped[ObjectType] = mapped_column(Enum(ObjectType))
#     object_id: Mapped[int] = mapped_column(db.Integer)  # ID связанного объекта
#     details: Mapped[str] = mapped_column(db.String(255), nullable=True)
#     created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

#     def __repr__(self):
#         return f"<Action: {self.action.value} {self.object_type.value}, Time: {self.created_at}>"
    


