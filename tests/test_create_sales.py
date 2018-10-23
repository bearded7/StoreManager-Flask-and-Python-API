import flask
import unittest
from flask import json
from unittest import TestCase
from endpoints.createsales import app


class TestIwoto4(unittest.TestCase):
    def test_client_can_create_sales_records(self):
        feedback = self.client.post(
                'StoreManager/api/v1/CreateSales'
                )
        self.assertEqual(200, feedback.status_code)

    def test_route_create_new_sales_records_requires_login(self):
        feedback = self.client.get(
                'StoreManager/api/v1/Sales', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', feedback.data)


if __name__ == '__main__':
    unittest.main()
