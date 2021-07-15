import unittest
import requests
from app import index, hello
from unittest.mock import patch
from database.booksdb import Database
import json


class TestBookShop_API(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000"  # extract into config file

    def test_root_page_returns_string_index_page(self):
        INDEX_ROUTE = "/"
        ENDPOINT_URL = f"{self.API_URL}{INDEX_ROUTE}"
        r = requests.get(ENDPOINT_URL)

        self.assertEqual(200, r.status_code)
        self.assertEqual("Index Page", r.text)

    def test_hello_route_returns_string_index_page(self):
        INDEX_ROUTE = "/hello"
        ENDPOINT_URL = f"{self.API_URL}{INDEX_ROUTE}"
        r = requests.get(ENDPOINT_URL)

        self.assertEqual(200, r.status_code)
        self.assertEqual("Hello World", r.text)

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
        INDEX_ROUTE = "/books?name=mey"
        ENDPOINT_URL = f"{self.API_URL}{INDEX_ROUTE}"
        r = requests.get(ENDPOINT_URL)

        json_object = json.loads(r.text)
        author_name = json_object['results'][0]['author'].lower()

        self.assertEqual(200, r.status_code)
        self.assertIn("mey", author_name)

    def test_should_return_books_containing_exact_price(self):
        INDEX_ROUTE = "/books?price=3409"
        ENDPOINT_URL = f"{self.API_URL}{INDEX_ROUTE}"
        r = requests.get(ENDPOINT_URL)

        json_object = json.loads(r.text)
        price = int(json_object['results'][0]['price'])
        self.assertEqual(200, r.status_code)
        self.assertEqual(3409, price)

    def test_should_return_books_containing_language_code(self):
        INDEX_ROUTE = "/books?language=en"
        ENDPOINT_URL = f"{self.API_URL}{INDEX_ROUTE}"

        r = requests.get(ENDPOINT_URL)
        json_object = json.loads(r.text)
        language = json_object['results'][0]['language_code'].lower()
        self.assertEqual(200, r.status_code)
        self.assertIn("en", language)

    def test_should_return_books_containing_isbn(self):
        INDEX_ROUTE = "/books?isbn=316"
        ENDPOINT_URL = f"{self.API_URL}{INDEX_ROUTE}"

        r = requests.get(ENDPOINT_URL)
        json_object = json.loads(r.text)
        isbn = json_object['results'][0]['isbn']
        self.assertEqual(200, r.status_code)
        self.assertIn("316", isbn)

    def test_should_return_books_containing_isbn13(self):
        INDEX_ROUTE = "/books?isbn13=978"
        ENDPOINT_URL = f"{self.API_URL}{INDEX_ROUTE}"

        r = requests.get(ENDPOINT_URL)
        json_object = json.loads(r.text)
        isbn = json_object['results'][0]['isbn13']
        self.assertEqual(200, r.status_code)
        self.assertIn("978", isbn)
