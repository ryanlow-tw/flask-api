import os


class Config(object):
    pass


class EnvironmentConfig(Config):
    username = os.getenv('DB_USERNAME')
    database_name = os.getenv('DB_NAME')
    password = os.getenv('DB_PASSWORD')
    port = 5432

    FLASK_ENV = "dev"
    SQLALCHEMY_DATABASE_URI = f'postgresql://{username}:{password}@postgres:{port}/{database_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/books.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
