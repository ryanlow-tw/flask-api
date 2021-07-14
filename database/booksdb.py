from sqlalchemy import create_engine, Table, MetaData, Column, Integer
from sqlalchemy.orm import mapper, sessionmaker


class Bookshop(object):
    pass


class Database:
    __instance = None

    @staticmethod
    def get_instance():
        if Database.__instance is None:
            Database()
        return Database.__instance

    def __init__(self, db_path, table_name):
        if Database.__instance is not None:
            raise Exception("Database cannot be instantiated more than once :(")

        else:
            Database.__instance = self
            self.db_path = db_path
            self.table_name = table_name
            self.session = None
            self.Bookshop = None

    def create_db_session(self):
        engine = create_engine(self.db_path)
        metadata = MetaData(engine)
        bookshop = Table(self.table_name, metadata, Column("id", Integer, primary_key=True), autoload=True)
        mapper(Bookshop, bookshop)
        session = sessionmaker(bind=engine)
        self.session = session()
        self.Bookshop = Bookshop
