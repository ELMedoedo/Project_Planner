from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from webapp.db import db  
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
    
    @property
    def is_admin(self):
        return self.role == "admin"