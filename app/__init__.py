from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import trigger_report_bp, get_report_bp
    app.register_blueprint(trigger_report_bp)
    app.register_blueprint(get_report_bp)

    return app
