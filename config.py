import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()


class Config:
    """
    Configuration class for the Flask application.
    """

    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        basedir, "store_monitoring.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
