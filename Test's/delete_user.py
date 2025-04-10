from database import db_session
from models import User

my_user = db_session.get(User, 5)
db_session.delete(my_user)
db_session.commit()