import logging
import os
from books_utils.books_utils import parse_books_query_strings
from flask import Flask, request
from database.booksdb import DatabaseConnection
from database.seed.seed_mongo import seed_database

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
port = os.getenv('DB_PORT')
host = os.getenv('DB_HOST')
mongo_url = f'mongodb://{username}:{password}@{host}:{port}'
seed_database(mongo_url, db_name)
connection = DatabaseConnection(mongo_url)
database = connection.load_db(db_name)
collections = database['books50']

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

logging.basicConfig(filename="./log.txt", level=logging.INFO)


@app.route('/')
def index():
    logging.info("This is the index page.")

    return "Index Page"


@app.route('/hello')
def hello():
    logging.info("This is the hello page.")

    return "Hello World"


@app.route('/books/<int:book_id>', methods=["GET"])
def books_id(book_id):
    query = {"id": book_id}

    results = collections.find(query, {'_id': 0})

    return {'results': [doc for doc in results]}


@app.route('/books', methods=["GET"])
def books():
    query_strings = request.args.to_dict()
    results = parse_books_query_strings(collections, query_strings)

    return {'results': [doc for doc in results]}


@app.route('/environment')
def environment():
    current_environment = os.environ.get('CURRENT_ENV')
    return f'This is {current_environment}'


@app.route('/test')
def test():
    return f'{__name__}'


if __name__ == '__main__':
    app.run()
