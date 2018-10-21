import unittest
import json
import requests 
from unittest import TestCase
from endpoints.createproduct import app 

def test_admin_can_add_product(self):
    response = self.admin.post(
        'StoreManager/api/v1/AddProducts/'
    )
    self.assertEqual(200, response.status_code)

def test_route_admin_can_add_product_requires_login(self):
    response = self.admin.get(
        'StoreManager/api/v1/Products/', follow_redirects=True)
    self.assertIn(b'Please log in to access this page', response.data)

if __name__ == '__main__':
    unittest.main()