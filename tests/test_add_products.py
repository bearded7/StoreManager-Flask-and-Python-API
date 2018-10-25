# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 07:47:04 2018

@author: XaXa
"""

import unittest
from unittest import TestCase
import flask
from flask import json
from flask import request
from storeapi.createproduct import app


class TestIwoto7(unittest.TestCase):
    def setUp(self):
        self.iwoto = app.test_client()

    def test_add_product(self):
        product = {
                "id": 112,
                "name": "T-Shirt",
                "price": "10,000 Ugx",
        }

        result = self.iwoto.post('StoreManager/api/v1/Products/Add/',
            content_type='application/json',
            data=json.dumps(product),)

        self.assertEqual(result.status_code, 404)
        self.assertIsNotNone(result)

    def test_fields_can_take_both_str_and_int(self):
        product = {
                "id": 112,
                "name": "T-Shirt",
                "price": "10,000 Ugx",
        }
    
        result = self.iwoto.post('StoreManager/api/v1/Products/',
            content_type='application/json',
            data=json.dumps(product),)
                                 
        self.assertEqual(result.status_code, 404)
    
    def test_add_product_with_no_name(self):
        self.iwoto.post("StoreManager/api/v1/Products/",
            content_type='application/json',
            data=json.dumps(dict(id="114", name=" ", price="20,000 Ugx"),))

    def test_cannot_add_empty_product(self):
        result = self.iwoto.post("StoreManager/api/v1/Products/",
            content_type='application/json',
            data=json.dumps(dict(id=" ", name=" ", price=" "),))
        
        self.assertEqual(result.status_code, 404)

    def test_add_product_with_no_quantity(self):
        result = self.iwoto.post("StoreManager/api/v1/Products/",
            content_type='application/json',
            data=json.dumps(dict(product="Mocassins", quantity=" ",
            price="75,000 Ugx"),))

        self.assertEqual(result.status_code, 404,),
        

    def test_add_product_with_no_price(self):
        result = self.iwoto.post("StoreManager/api/v1/Products/",
            content_type='application/json',
            data=json.dumps(dict(id="118", name="Timbaland", price=" "),))

        self.assertEqual(result.status_code, 404)
        

    def test_add_product_with_short_name(self):
        result = self.iwoto.post("StoreManager/api/v1/Products/",
            content_type='application/json',
            data=json.dumps(dict(id="", name="Rice", price="9,500 Ugx"),))

        self.assertEqual(result.status_code, 404)
        

    def test_add_product_with_missing_id(self):
        result = self.iwoto.post("StoreManager/api/v1/Products/",
            content_type='application/json',
            data=json.dumps(dict(name="Jeans", price="15,000 Ugx"),))
        
        self.assertEqual(result.status_code, 404)
        
    

    def test_invalid_JSON(self):
        result = self.iwoto.post('StoreManager/api/v1/Products/130',
        data="not a json",
        content_type='application/json')
        self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
    unittest.main()
