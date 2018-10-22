import unittest
import json
import requests 
from unittest import TestCase
from endpoints.sales_by_id import app

def test_client_can_get_own_sale_records(self):
    id = 1110
    id = 1113
    id = 1115

    feedback = self.client.get(
        'StoreManager/api/v1/ProductsSales/%d' %id,
    )
    data = json.loads(feedback.data)
    print(data)
    print(feedback.status_code)
    self.assertEqual(200, feedback.status_code, msg = "Here is your sale record")

def test_route_get_own_sales_requires_login(self):
    feedback = self.client.get(
        'StoreManager/api/v1/Sales/', follow_redirects=True)
    self.assertIn(b'Please log in to access this page', feedback.data)

if __name__ == '__main__':
    unittest.main()