from pymongo import MongoClient


class DatabaseConnection:
    __instance = None

    @staticmethod
    def get_instance():
        if DatabaseConnection.__instance is None:
            DatabaseConnection()
        return DatabaseConnection.__instance

    def __init__(self, url):
        if DatabaseConnection.__instance is not None:
            raise Exception("Database cannot be instantiated more than once :(")

        else:
            DatabaseConnection.__instance = self
            self.url = url

    def load_db(self, db_name):

        client = MongoClient(self.url)
        mongo_database = client[db_name]
        return mongo_database
