import unittest
import json
import requests 
from unittest import TestCase

def test_admin_and_attendant_can_get_products(self):
    res = self.client.get(
        'StoreManager/api/v1/GetAllProducts'
    )
    self.assertEqual(200, res.status_code)

    res = self.admin.get (
        'StoreManager/api/v1/GetAllProducts'
    )
    self.assertEqual(200, res.status_code)

if __name__ == '__main__':
    unittest.main()