import unittest
import requests


class TestBookShop_API(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000"

    def test_root_page_returns_string_index_page(self):
        INDEX_ROUTE = "/"
        ENDPOINT_URL = f"{self.API_URL}{INDEX_ROUTE}"
        r = requests.get(ENDPOINT_URL)

        self.assertEqual(200, r.status_code)
        self.assertEqual("Index Page", r.text)

