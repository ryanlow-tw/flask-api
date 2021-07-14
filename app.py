from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from database.booksdb import Database
from db_parser.db_parser import parse_data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

books_50 = db.Table('books_50', db.metadata, autoload=True, autoload_with=db.engine)
bookshop = Database(books_50)

logging.basicConfig(filename="./log.txt", level=logging.INFO)


@app.route('/')
def index():
    logging.info("This is the index page.")
    return "Index Page"


@app.route('/hello')
def hello():
    logging.info("This is the hello page.")
    return "Hello World"


@app.route('/books', methods=["GET"])
def books():
    results = db.session.query(bookshop.db).all()
    return {'results': parse_data(results)}


if __name__ == '__main__':
    app.run(debug=True)
