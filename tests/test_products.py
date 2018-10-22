import unittest
import json
import requests 
from unittest import TestCase
from endpoints.all_products import app

def test_admin_and_attendant_can_get_products(self):
    response = self.client.get(
        'StoreManager/api/v1/GetAllProducts'
    )
    self.assertEqual(404, response.status_code)

    response = self.admin.get (
        'StoreManager/api/v1/GetAllProducts'
    )
    self.assertEqual(404, response.status_code)

if __name__ == '__main__':
    unittest.main()