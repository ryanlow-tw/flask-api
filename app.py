from flask import Flask
import logging
from database.booksdb import Database

db_path = 'sqlite:///database/books.db'
table_name = 'books_50'
bookshop = Database(db_path, table_name)
bookshop.create_db_session()
res = bookshop.session.query(bookshop.Bookshop).all()
print(res[0].author)
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


@app.route('/books', methods=["GET"])
def books():
    return


if __name__ == '__main__':
    app.run(debug=True)
