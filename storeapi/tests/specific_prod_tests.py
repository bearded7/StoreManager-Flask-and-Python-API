import unittest
import json
import requests 
from unittest import TestCase

def test_both_admin_attendant_can_get_specific_product(self):
    id = 110
    id = 111
    id = 112
    id = 113
    id = 114
    id = 115

    res = self.client.get(
        'StoreManager/api/v1/Products/%d' %id,
    )
    data = json.loads(res.data)
    print(data)
    print(res.status_code)
    self.assertEqual(200, res.status_code, msg = "product located")

def test_cannot_get_invalid_product_id(self):
    self.product_url = "http://localhost:5000/StoreManager/api/v1/Products/1"
    res = self.client.get(self.product_url)
    self.assertEqual(404, res.status_code)

if __name__ == '__main__':
    unittest.main()