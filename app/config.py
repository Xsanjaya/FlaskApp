import os

class AppConfig:
    SECRET_KEY = os.urandom(32)

    # Grabs the folder where the script runs.
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Enable debug mode.
    DEBUG = False

    # Connect to the database
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_SQLITE')

    # Turn off the Flask-SQLAlchemy event system and warning
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class Settings:
    JWT_SECRET = os.getenv('JWT_SECRET')
    JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256') 