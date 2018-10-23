import flask
import unittest
from flask import json
from unittest import TestCase
from endpoints.createsales import app


class TestIwoto4(unittest.TestCase):
    def recSet(self):
        self.client = app.test_client()

    def test_add_sale(self):
        sale = {
            "id": 116,
            "product_name": "maize",
            "unit price": "12,000 Ugx per Kg",
            "quantity": "1 KG",
            "total price": "12,000 Ugx",
        }

        result = self.client.post('StoreManager/api/v1/Sales/Create/',
                                  content_type='application/json',
                                  data=json.dumps(sale)
                                  )

        self.assertEqual(result.status_code, 404)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
