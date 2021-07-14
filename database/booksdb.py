class Database:
    __instance = None

    @staticmethod
    def get_instance():
        if Database.__instance is None:
            Database()
        return Database.__instance

    def __init__(self, db):
        if Database.__instance is not None:
            raise Exception("Database cannot be instantiated more than once :(")

        else:
            Database.__instance = self
            self.db = db
