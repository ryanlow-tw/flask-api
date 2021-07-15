class Database:
    __instance = None

    @staticmethod
    def get_instance():
        if Database.__instance is None:
            Database()
        return Database.__instance

    def __init__(self, db, table_name):
        if Database.__instance is not None:
            raise Exception("Database cannot be instantiated more than once :(")

        else:
            Database.__instance = self
            self.db = db
            self.table_name = table_name

    def load_db(self):
        self.db = self.db.Table(self.table_name,
                                self.db.metadata,
                                autoload=True,
                                autoload_with=self.db.engine)
