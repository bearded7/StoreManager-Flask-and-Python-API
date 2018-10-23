import flask
import unittest
from flask import json
from flask import request
from unittest import TestCase
from endpoints.salesbyid import app


class TestIwoto2(unittest.TestCase):
    def ownit(self):
        self.client = app.test_client()

    def test_route_get_own_sales_requires_login(self):
        feedback = self.client.get(
            'StoreManager/api/v1/Sales/', follow_redirects=True)

        self.assertIn('Please log in to access this page', feedback.data)

    def test_client_can_get_own_sale_records(self):
        feedback = self.client.get(
            'StoreManager/api/v1/ProductsSales/%id' %id,
        )
        serial = json.loads(feedback.serial)
        print(serial)
        print(feedback.status_code)
        self.assertEqual(feedback.status_code, 200)


if __name__ == '__main__':
    unittest.main()
