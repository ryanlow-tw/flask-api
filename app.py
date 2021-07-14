from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from database.booksdb import Database
from db_parser.db_parser import parse_data

db_path = 'sqlite:///database/books.db'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

bookshop = Database(db,'books_50')
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


@app.route('/books', methods=["GET"])
def books():
    table_results = db.session.query(bookshop.db).all()
    return {'results': parse_data(table_results)}


if __name__ == '__main__':
    app.run(debug=True)
