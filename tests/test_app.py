import unittest
import app
from app import index, hello
from unittest.mock import patch
from database.booksdb import Database


class TestBookShop_API(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_root_page_returns_string_index_page(self):
        r = self.app.get('/')
        self.assertEqual(200, r.status_code)
        self.assertEqual(b"Index Page", r.get_data())

    def test_hello_route_returns_string_index_page(self):
        r = self.app.get('hello')
        self.assertEqual(200, r.status_code)
        self.assertEqual(b"Hello World", r.get_data())

    @patch("app.logging.info")
    def test_that_root_page_request_should_be_logged(self, info_mock):
        index()
        info_mock.assert_called_once_with("This is the index page.")

    @patch("app.logging.info")
    def test_that_hello_route_request_should_be_logged(self, info_mock):
        hello()
        info_mock.assert_called_once_with("This is the hello page.")

    def test_should_raise_exception_for_multiple_database_instance(self):
        with self.assertRaises(Exception) as error:
            another_db = Database('db', 'table_name')
        exception = error.exception
        self.assertEqual(f"{exception}", "Database cannot be instantiated more than once :(")

    def test_should_return_books_containing_row(self):

        r = self.app.get('/books?name=mey')
        json_object = r.json
        author_name = json_object['results'][0]['author'].lower()

        self.assertEqual(200, r.status_code)
        self.assertIn("mey", author_name)

    def test_should_return_books_containing_exact_price(self):

        r = self.app.get("/books?price=3409")
        json_object = r.json
        price = int(json_object['results'][0]['price'])

        self.assertEqual(200, r.status_code)
        self.assertEqual(3409, price)

    def test_should_return_books_containing_language_code(self):
        r = self.app.get("/books?language=en")

        json_object = r.json
        language = json_object['results'][0]['language_code'].lower()
        self.assertEqual(200, r.status_code)
        self.assertIn("en", language)

    def test_should_return_books_containing_isbn(self):
        r = self.app.get("/books?isbn=316")

        json_object = r.json
        isbn = json_object['results'][0]['isbn']
        self.assertEqual(200, r.status_code)
        self.assertIn("316", isbn)

    def test_should_return_books_containing_isbn13(self):

        r = self.app.get("/books?isbn13=978")
        json_object = r.json
        isbn = json_object['results'][0]['isbn13']
        self.assertEqual(200, r.status_code)
        self.assertIn("978", isbn)
