import unittest
import requests
from app import index, hello
from unittest.mock import patch
from database.database import Database


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

    @patch("bookshop_api.logging.info")
    def test_that_root_page_request_should_be_logged(self, info_mock):
        index()
        info_mock.assert_called_once_with("This is the index page.")

    @patch("bookshop_api.logging.info")
    def test_that_hello_route_request_should_be_logged(self, info_mock):
        hello()
        info_mock.assert_called_once_with("This is the hello page.")

    def test_should_raise_exception_for_multiple_database_instance(self):

        with self.assertRaises(Exception) as error:
            another_db = Database()
        exception = error.exception
        self.assertEqual(f"{exception}", "Database cannot be instantiated more than once :(")

