# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:35:51 2018

@author: XaXa
"""

import flask
import unittest
from flask import json
from unittest import TestCase
from storeapi.all_products import app


products = [
 {

  'id': '110',

  'name': 'Rice',

  'Price': '7,500 Ugx'

 },

 {

  'id': '111',

  'name': 'Mocassins',

  'Price': '75,000 Ugx'

 },

 {

  'id': '112',

  'name': 'T-Shirt',

  'Price': '10,000 Ugx'

 },

 {

  'id': '113',

  'name': 'Timbaland',

  'Price': '150,000 Ugx'

 },

 {

  'id': '114',

  'name': 'Maize Flour',

  'Price': '80,000 Ugx'

 },

 {

  'id': '115',

  'name': 'Jean Trousers',

  'Price': '30,000 Ugx'

 }

 ]

class TestIwoto3(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        
    def test_get_all_products(self):
        products = self.client.get('StoreManager/api/v1/Products/All/')
        self.assertEqual(products.status_code, 404)

    def test_cannot_add_nonJSON(self):
        products = self.client.post('/StoreManager/api/v1/Sale_records',
                                    data="This is a string! It's not JSON!")
        self.assertEqual(products.status_code, 404)


if __name__ == '__main__':
    unittest.main()
