from flask import Flask
import logging
from database.booksdb import Database

db_path = 'sqlite:///database/books.db'
table_name = 'books_50'
bookshop = Database(db_path, table_name)
bookshop.create_db_session()

books_list = []

for instance in bookshop.session.query(bookshop.Bookshop).all():
    books_list.append({
        'id': f'{instance.id}',
        'author': f'{instance.author}',
        'title': f'{instance.title}',
        'image_url': f'{instance.image_url}',
        'small_image_url': f'{instance.small_image_url}',
        'price': f'{instance.price}',
        'isbn': f'{instance.isbn}',
        'isbn13': f'{instance.isbn13}',
        'original_publication_year': f'{instance.original_publication_year}',
        'original_title': f'{instance.original_title}',
        'language_code': f'{instance.language_code}',
        'average_rating': f'{instance.average_rating}'})

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
    return {'results': books_list}


if __name__ == '__main__':
    app.run(debug=True)
