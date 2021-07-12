import logging
import unittest
import requests
from bookshop_api import index, hello
from unittest.mock import patch


class TestBookShop_API(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000"

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