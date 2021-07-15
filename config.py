class Config(object):
    pass


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/books.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    pass
