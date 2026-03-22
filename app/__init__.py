# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Tell Flask-Login where to redirect if user is not logged in
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # Register Blueprints (routes)
    from app.routes.auth import auth
    from app.routes.student import student
    from app.routes.admin import admin

    app.register_blueprint(auth)
    app.register_blueprint(student)
    app.register_blueprint(admin)

    return app