# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:07:16 2018

@author: XaXa
"""


import unittest
from flask import json
from storeapi.api import App


class TestIwoto(unittest.TestCase):
    def setUp(self):
        self.client = App.test_client()

    def test_base_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_all_products(self):
        result = self.client.get('StoreManager/api/v1/Products/All/')
        self.assertEqual(result.status_code, 200)

    def test_fetch_specific_product(self):
        result = self.client.get('StoreManager/api/v1/Products/<productId')
        self.assertEqual(result.status_code, 200)

    def test_unavailable_product_fetch(self):
        result = self.client.get('StoreManager/api/v1/Products/')
        self.assertEqual(result.status_code, 404)

    def test_add_product(self):
        product = {
                'id': '112',
                'name': 'T-Shirt',
                'Price': '10,000 Ugx'
        }

        result = self.client.post('StoreManager/api/v1/Products/Add/',
                                  content_type='application/json',
                                  data=json.dumps(product)
                                  )

        self.assertEqual(result.status_code, 201)
        self.assertIsNotNone(result)

    def test_get_all_sales(self):
        result = self.client.get('StoreManager/api/v1/Sales/All/')
        self.assertEqual(result.status_code, 404)

    def test_fetch_specific_sale(self):
        result = self.client.get('StoreManager/api/v1/Sales/<salesId')
        self.assertEqual(result.status_code, 200)

    def test_unavailable_sales_fetch(self):
        result = self.client.get('StoreManager/api/v1/Sales/')
        self.assertEqual(result.status_code, 404)

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
