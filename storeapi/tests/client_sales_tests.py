import unittest
import json
import requests 
from unittest import TestCase

def test_client_can_get_own_sale_records(self):
    id = 1110
    id = 1113
    id = 1115

    res = self.client.get(
        'StoreManager/api/v1/ProductsSales/%d' %id,
    )
    data = json.loads(res.data)
    print(data)
    print(res.status_code)
    self.assertEqual(200, res.status_code, msg = "Here is your sale record")

def test_route_get_own_sales_requires_login(self):
    res = self.client.get(
        'StoreManager/api/v1/Sales', follow_redirects=True)
    self.assertIn(b'Please log in to access this page', response.data)

if __name__ == '__main__':
    unittest.main()