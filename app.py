from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from database.booksdb import Database
from db_parser.db_parser import parse_data
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

    order = query_strings.get("order", "").lower()
    name = query_strings.get("name", "").lower()
    price = query_strings.get("price", None)
    language = query_strings.get("language", "").lower()
    isbn = query_strings.get("isbn", "")
    isbn13 = query_strings.get("isbn13", "")

    if name != "":
        query_builder = query_builder.filter(bookshop.db.c.author.contains(name))

    if price is not None:
        price = int(price)
        query_builder = query_builder.filter(bookshop.db.c.price.contains(price))

    if language != "":
        query_builder = query_builder.filter(bookshop.db.c.language_code.contains(language))

    if isbn != "":
        query_builder = query_builder.filter(bookshop.db.c.isbn.contains(isbn))

    if isbn13 != "":
        query_builder = query_builder.filter(bookshop.db.c.isbn13.contains(isbn13))

    if order == "desc":
        query_builder = query_builder.order_by(bookshop.db.c.price.desc()).all()
    elif order == "asc":
        query_builder = query_builder.order_by(bookshop.db.c.price).all()
    else:
        query_builder = query_builder.all()
    data = parse_data(query_builder)
    return data


if __name__ == '__main__':
    app.run(debug=True)
