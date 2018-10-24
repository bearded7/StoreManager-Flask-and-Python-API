# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 23:15:38 2018

@author: XaXa
"""

import flask
import unittest
from flask import json
from unittest import TestCase
from storeapi.createsales import app


class TestIwoto4(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add_sale(self):
        sale = {
            "id": 1116,
            "product_name": "soya",
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
    
    def test_cannot_add_nonJSON(self):
        response = self.client.post('StoreManager/api/v1/Sales/Create/',
                                    data="This is a string! It's not JSON!")
        self.assertEqual(response.status_code, 404)

    def test_cannot_add_empty_Sale_order(self):
        response = self.client.get('StoreManager/api/v1/Sales/Create/')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
