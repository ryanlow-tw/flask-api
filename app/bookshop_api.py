from flask import Flask
import logging
import sqlite3

db_path = "../database/books.db"
app = Flask(__name__)
logging.basicConfig(filename="../log.txt", level=logging.INFO)


@app.route('/')
def index():
    logging.info("This is the index page.")
    return "Index Page"


@app.route('/hello')
def hello():
    logging.info("This is the hello page.")
    return "Hello World"


@app.route('/books')
def books():
    query = "SELECT * FROM books_50"
    return get_data(query)


def get_data(query):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        json_results = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
        return {"result": json_results}


if __name__ == '__main__':
    app.run(debug=True)
