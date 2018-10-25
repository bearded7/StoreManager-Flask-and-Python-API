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

new_sales = [{}]

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
    
    def test_cannot_add_empty_Sale_order(self):
        new_sales = self.client.post('/StoreManager/api/v1/Sale/Create/',
        data=json.dumps(
            {
                'id': '',
                'name': '',
                'unit price': '',
                'quantity': '',
                'total price': ''

            }),
            content_type='application/json')

        self.assertEqual(new_sales.status_code, 404)

    def test_client_add_sale_record(self):
        new_sales = self.client.post('/StoreManager/api/v1/Sale/Create/',
        data=json.dumps(
            {
                'id': '1120',
                'name': 'Soya',
                'unit price': '12,000 Ugx',
                'quantity': '2',
                'total price': '24,000 Ugx'

            }),
            content_type='application/json')

        self.assertEqual(new_sales.status_code, 404)
                                    
    def test_int_str_accepted(self):
        new_sales = self.client.post('/StoreManager/api/v1/Sale/Create/',
        data=json.dumps(
            {
                'id': '1119',
                'name': 'Fanta',
                'unit price': '1,200 Ugx',
                'quantity': '7 bottles',
                'total price': '8,400 Ugx'

            }),
            content_type='application/json')

        self.assertEqual(new_sales.status_code, 404)

    def test_cannot_add_nonJSON(self):
        new_sales = self.client.post(
            '/StoreManager/api/v1/Sale_records',
            data="This is a string! It's not JSON!")                           
        self.assertEqual(new_sales.status_code, 404)


if __name__ == '__main__':
    unittest.main()
