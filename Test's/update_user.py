from sqlalchemy import select

from database import db_session
from models import User

my_user = select(User).where(User.user=="Test1")
Test1 = db_session.execute(my_user).scalar()

Test1.email = "Test3@i.p"

db_session.commit()