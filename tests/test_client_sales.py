# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 01:15:38 2018

@author: XaXa
"""

import flask
import unittest
from flask import json
from flask import request
from unittest import TestCase
from storeapi.salesbyid import app


sales = [

 {

  'id': '1110',

  'product': 'Rice',

  'unit price': '7,500 Ugx',

  'quantity': 5,

  'total price': '37,500 Ugx'

 },

 {

  'id': '1111',

  'product': 'T-shirt',

  'unit price': '10,000 Ugx',

  'quantity': 4,

  'total price': '40,000 Ugx'

 },

 {

  'id': 1112,

  'product': 'Mocassins',

  'unit price': '75,000 Ugx',

  'quantity': 2,

  'total price': '150,000 Ugx'

 },

 {

  'id': '1113',

  'product': 'Timbaland',

  'unit price': '150,000 Ugx',

  'quantity': 2,

  'total price': '300,000 Ugx'

 },

 {

  'id': '1114',

  'product': 'Maize flour',

  'unit price': '80,000 Ugx',

  'quantity': 10,

  'total price': '800,000 Ugx'

 },

 {

  'id': '1115',

  'product': 'Jean Trousers',

  'unit price': '30,000 Ugx',

  'quantity': 15,

  'total price': '450,000 Ugx'

 },

 ]

class TestIwoto2(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_fetch_owner_sale_records(self):
        result = self.client.get('/StoreManager/api/v1/Sales/All')
        self.assertEqual(result.status_code, 401)

    def test_want_to_see_own_sales_records(self):
        result = self.client.get('/StoreManager/api/v1/Sales/')
        self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
    unittest.main()
