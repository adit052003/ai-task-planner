# app/__init__.py

from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db, migrate, login, jwt  # Import extensions
from flask_mail import Mail
import os

mail = Mail()  # Add this with other extensions

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Add Mail configuration
    app.config.update(
        MAIL_SERVER = 'smtp.gmail.com',
        MAIL_PORT = 587,
        MAIL_USE_TLS = True,
        MAIL_USERNAME = os.getenv('EMAIL_USER'),
        MAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    )

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)  # Initialize mail
    CORS(app)  # Make sure CORS is enabled

    # Import models
    from app import models

    # Register blueprints
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.ai_routes import ai as ai_blueprint
    app.register_blueprint(ai_blueprint, url_prefix='/api')  # Add url_prefix if needed

    return app