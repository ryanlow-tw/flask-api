from flask import Flask
import logging

app = Flask(__name__)


@app.route('/')
def index():
    return "Index Page"


@app.route('/hello')
def hello():
    return "Hello World"


def run_app():
    logging.basicConfig(filename="log.txt", level=logging.INFO)
    app.run()

if __name__ == '__main__':
    run_app()

