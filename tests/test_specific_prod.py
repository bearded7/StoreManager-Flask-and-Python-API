import unittest
import json
import requests
from unittest import TestCase
from endpoints.single_product import app


class TestIwoto6(unittest.TestCase):
    def locatEm(self):
        self.client = app.test_client()
        
    def test_both_admin_attendant_can_get_specific_product(self):
        feedback = self.client.get(
                'StoreManager/api/v1/Products/%d' %id,
                )
        data = json.loads(feedback.data)
        print(data)
        print(feedback.status_code)
        self.assertEqual(200, feedback.status_code)

    def test_cannot_get_invalid_product_id(self):
        self.product_url = "http://localhost:5000/StoreManager/api/v1/Products/1"
        feedback = self.client.get(self.product_url)
        self.assertEqual(404, feedback.status_code)


if __name__ == '__main__':
    unittest.main()
