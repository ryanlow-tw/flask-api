class Config(object):
    pass


class EnvironmentConfig(Config):
    FLASK_ENV = "dev"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/books.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
