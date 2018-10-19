import unittest
import json
import requests 
from unittest import TestCase

def test_admin_can_get_all_sale_records(self):
    res = self.admin.get(
        'StoreManager/api/v1/GetAllSales'
    )
    self.assertEqual(200, res.status_code)

def test_route_get_all_sales_requires_login(self):
    res = self.admin.get(
        'StoreManager/api/v1/GetAllSales', follow_redirects=True)
    self.assertIn(b'Please log in to access this page', response.data)

if __name__ == '__main__':
    unittest.main()