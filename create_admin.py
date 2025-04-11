from getpass import getpass # скрывание пароля из отображания (звездочки вместо пароля)
import sys  # модуль взаимодействия с системными вызовами

from webapp import create_app
from webapp.model import User, db

app = create_app()
