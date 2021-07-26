import unittest
import requests
from database.booksdb import DatabaseConnection


class TestBookShop_API(unittest.TestCase):

    def test_root_page_returns_string_index_page(self):
        r = requests.get('http://bookshop:5000')
        self.assertEqual(200, r.status_code)
        self.assertEqual("Index Page", r.text)

    def test_hello_route_returns_string_index_page(self):
        r = requests.get('http://localhost:5000/hello')
        self.assertEqual(200, r.status_code)
        self.assertEqual("Hello World", r.text)

    def test_should_raise_exception_for_multiple_database_instance(self):
        with self.assertRaises(Exception) as error:
            one_db = DatabaseConnection('self.mongo_url')
            another_db = DatabaseConnection('self.mongo_url')
        exception = error.exception
        self.assertEqual(f"{exception}", "Database cannot be instantiated more than once :(")

    def test_should_return_books_containing_row(self):
        r = requests.get('http://localhost:5000/books?author=mey')
        json_object = r.json()
        author_name = json_object['results'][0]['author'].lower()

        self.assertEqual(200, r.status_code)
        self.assertIn("mey", author_name)

    def test_should_return_books_containing_exact_price(self):
        r = requests.get("http://localhost:5000/books?price=3409")
        json_object = r.json()
        price = int(json_object['results'][0]["price"])

        self.assertEqual(200, r.status_code)
        self.assertEqual(3409, price)

    def test_should_return_books_containing_language_code(self):
        r = requests.get("http://localhost:5000/books?language_code=en")

        json_object = r.json()
        language = json_object['results'][0]['language_code'].lower()
        self.assertEqual(200, r.status_code)
        self.assertIn("en", language)

    def test_should_return_books_containing_isbn(self):
        r = requests.get("http://localhost:5000/books?isbn=316")

        json_object = r.json()
        isbn = json_object['results'][0]['isbn']
        self.assertEqual(200, r.status_code)
        self.assertIn("316", isbn)

    def test_should_return_books_containing_isbn13(self):
        r = requests.get("http://localhost:5000/books?isbn13=978")
        json_object = r.json()
        isbn = json_object['results'][0]['isbn13']
        self.assertEqual(200, r.status_code)
        self.assertIn("978", isbn)
