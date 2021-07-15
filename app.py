from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from database.booksdb import Database
from db_parser.db_parser import parse_data, parse_query
import logging

db_path = 'sqlite:///database/books.db'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
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
    table_results = db.session.query(bookshop.db).filter_by(id=book_id).all()
    data = parse_data(table_results)
    return data


@app.route('/books', methods=["GET"])
def books():

    query_strings = request.args.to_dict()
    query_builder = db.session.query(bookshop.db)
    query_builder = parse_query(query_strings, query_builder, database=bookshop.db)
    data = parse_data(query_builder)

    return data


if __name__ == '__main__':
    app.run(debug=True)
