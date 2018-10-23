import unittest
import json
import requests
from unittest import TestCase
from endpoints.single_product import app


class TestIwoto6(unittest.TestCase):
    def locatEm(self):
        self.client = app.test_client()
        
    def test_fetch_specific_product(self):
        result = self.client.get('StoreManager/api/v1/Products/<productId')
        self.assertEqual(result.status_code, 200)

    def test_unavailable_product_fetch(self):
        result = self.client.get('StoreManager/api/v1/Products/')
        self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
    unittest.main()
