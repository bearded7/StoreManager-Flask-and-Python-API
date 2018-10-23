import flask
import unittest
from flask import json
from flask import request
from unittest import TestCase
from endpoints.salesbyid import app


class TestIwoto2(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_fetch_owner_sale_records(self):
        result = self.client.get('StoreManager/api/v1/Sales/<salesId>')
        self.assertEqual(result.status_code, 401)

    def test_want_to_see_unauthorized_sales_records(self):
        result = self.client.get('StoreManager/api/v1/Sales/')
        self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
    unittest.main()
