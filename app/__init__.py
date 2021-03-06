from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from app.models import UserModel
# app
from .config import Config
from .auth import auth

login_manger = LoginManager()
login_manger.login_view = 'auth.login'

@login_manger.user_loader
def load_user(username):
    return UserModel.query(username)


def create_app(enviroment):
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)

    login_manger.init_app(app)

    app.register_blueprint(auth)

    app.config.from_object(enviroment)

    return app