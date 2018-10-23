import flask
import unittest
from flask import json
from unittest import TestCase
from endpoints.all_products import app


class TestIwoto3(unittest.TestCase):
    def fetchEm(self):
        self.client = app.test_client()
        
    def test_get_all_products(self):
        result = self.client.get('StoreManager/api/v1/Products/All/')
        self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
    unittest.main()
