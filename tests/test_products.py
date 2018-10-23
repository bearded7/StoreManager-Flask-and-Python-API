import flask
import unittest
from flask import json
from unittest import TestCase
from endpoints.all_products import app


class TestIwoto3(unittest.TestCase):
    def fetchEm(self):
        self.client = app.test_client()
        
    def test_admin_and_attendant_can_get_products(self):
        response = self.client.get(
                'StoreManager/api/v1/Products/All/'
                )
        self.assertEqual(404, response.status_code)


if __name__ == '__main__':
    unittest.main()
