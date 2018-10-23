import unittest
import json
import requests
from unittest import TestCase
from endpoints.sales import app


class TestIwoto5(unittest.TestCase):
    def saleIt(self):
        self.client = app.test_client()

    def test_get_all_sales_recs(self):
        result = self.client.get('StoreManager/api/v1/Sales/All/')
        self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
    unittest.main()
