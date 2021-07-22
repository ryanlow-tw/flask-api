class Config(object):
    pass

class EnvironmentConfig(Config):
    username = 'postgres'
    database_name = username
    password = 'mysecretpassword'
    port = 5432

    FLASK_ENV = "dev"
    SQLALCHEMY_DATABASE_URI = f'postgresql://{username}:{password}@postgres:{port}/{database_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
