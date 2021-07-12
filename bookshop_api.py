from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(filename="log.txt", level=logging.INFO)


@app.route('/')
def index():
    logging.info("This is the index page.")
    return "Index Page"


@app.route('/hello')
def hello():
    logging.info("This is the hello page.")
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)
