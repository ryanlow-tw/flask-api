import sqlite3


class Database:
    __instance = None
    db_path = "../database/books.db"

    @staticmethod
    def get_instance():
        if Database.__instance is None:
            Database()
        return Database.__instance

    def __init__(self):
        if Database.__instance is not None:
            raise Exception("Database cannot be instantiated more than once :(")

        else:
            Database.__instance = self

    def get_data(self, query):
        with sqlite3.connect(Database.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            # cursor.description[i][0] gives the names of all columns
            json_results = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in
                            cursor.fetchall()]
            return {"result": json_results}
