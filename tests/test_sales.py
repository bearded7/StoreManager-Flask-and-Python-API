import unittest
import json
import requests
from unittest import TestCase
from endpoints.sales import app


class TestIwoto5(unittest.TestCase):
    def saleIt(self):
        self.client = app.test_client()

    def test_route_get_all_sales_requires_login(self):
        feedback = self.client.get(
                'StoreManager/api/v1/Sales, follow_redirects=True'
                )
        self.assertIn('Please log in to access this page', feedback.data)

    def test_admin_can_get_all_sale_records(self):
        feedback = self.client.get(
            'StoreManager/api/v1/Sales/All/'
        )
        self.assertEqual(feedback.status_code, 404)


if __name__ == '__main__':
    unittest.main()
