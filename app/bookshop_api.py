from flask import Flask, request
import logging
from database import Database

db = Database()
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
    order = request.args.get("order")
    limit = request.args.get("limit")


    query = f"SELECT * FROM books_50 ORDER BY price {order} LIMIT {limit}"
    return db.get_data(query)




if __name__ == '__main__':
    app.run(debug=True)
