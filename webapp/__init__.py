from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import logging

from webapp.db import db
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint
from webapp.tasks.views import blueprint as task_blueprint
from webapp.admin.views import blueprint as admin_blueprint

logging.basicConfig(filename="Planner.log", level=logging.INFO)


def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    migrate = Migrate(app, db)
    

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(user_blueprint)
    app.register_blueprint(task_blueprint)
    app.register_blueprint(admin_blueprint)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    return app
