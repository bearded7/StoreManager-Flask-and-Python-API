import unittest
import json
import requests 
from createsales import sales
from unittest import TestCase

def test_client_can_create_sales_records(self):
    res = self.client.post(
        'StoreManager/api/v1/CreateSales'
    )
    self.assertEqual(200, res.status_code)

def test_route_create_new_sales_records_requires_login(self):
    res = self.client.get(
        'StoreManager/api/v1/Sales', follow_redirects=True)
    self.assertIn(b'Please log in to access this page', response.data)

if __name__ == '__main__':
    unittest.main()
