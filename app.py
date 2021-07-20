from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from database.booksdb import Database
from books_utils.books_utils import format_data, parse_book_query_string
import logging
import os

app = Flask(__name__)
app.config.from_object('config.EnvironmentConfig')
db = SQLAlchemy(app)

bookshop = Database(db, 'books_50')
bookshop.load_db()

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

    data = db.session.query(bookshop.db).filter_by(id=book_id).all()
    result = format_data(data)

    return result


@app.route('/books', methods=["GET"])
def books():

    query_strings = request.args.to_dict()
    query_builder = db.session.query(bookshop.db)
    query_builder = parse_book_query_string(query_strings, query_builder, database=bookshop.db)
    data = format_data(query_builder)

    return data


@app.route('/environment')
def environment():

    current_environment = os.environ.get('CURRENT_ENV')
    return f'This is {current_environment}'


if __name__ == '__main__':
    app.run(debug=True)
