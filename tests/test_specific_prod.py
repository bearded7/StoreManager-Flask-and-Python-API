# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:25:02 2018

@author: XaXa
"""

import unittest
import json
import requests
from unittest import TestCase
from storeapi.single_product import app


class TestIwoto6(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        
    def test_fetch_product(self):
        result = self.client.get('StoreManager/api/v1/Products/<productId>')
        self.assertEqual(result.status_code, 404)
    
    def test_fetch_product_using_id(self):
        result = self.client.get('StoreManager/api/v1/Products/115')
        self.assertEqual(result.status_code, 400)
        self.client.post('/StoreManager/api/v1/Products/',
        data =json.dumps(
           {'id': '112',
           'name': 'T-Shirt',
           'Price': '10,000 Ugx'}
        ),
        content_type='application/json')
        created= self.client.get('/StoreManager/api/v1/Products/114')
        print(created)
        self.assertIsNotNone(created)
        display=json.loads(created.data)
        self.assertEqual('T-Shirt', display['name'])


    def test_fetching_products(self):
        response = self.client.post("StoreManager/api/v1/Products/",
            content_type='application/json',
            data=json.dumps(dict(product="Shirts", quantity="20", unit_price="200"),))

        reply = json.loads(response.data.decode())
        response2 = self.client.get("StoreManager/api/v1/Products/",
        content_type='application/json')
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(response2.status_code, 200)

    def test_fetching_single_product(self):
        response = self.client.post("StoreManager/api/v1/Products/",
            content_type='application/json',
            data=json.dumps(dict(product="Shirts", quantity="20", unit_price="200"),))

        reply = json.loads(response.data.decode())
        response2 = self.client.get("/api/v1/products/1",
        content_type='application/json')
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(response2.status_code, 200)

    def test_fetching_not_exist_single_product(self):
        response = self.client.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Shirts", quantity="20", unit_price="200"),))

        reply = json.loads(response.data.decode())
        response2 = self.client.get("/api/v1/products/12",
        content_type='application/json')
        reply2 = json.loads(response2.data)
        self.assertEquals(response2.status_code, 404)    

    def test_fetching_single_product_with_impromper_id(self):
        response = self.client.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Shirts", quantity="20", unit_price="200"),))

        reply = json.loads(response.data)
        response2 = self.client.get("/api/v1/products/q",
        content_type='application/json')
        reply2 = json.loads(response2.data)
        self.assertEquals(response2.status_code, 400)

    def test_fetch_unavailable_product(self):
        result = self.client.get('StoreManager/api/v1/Products/')
        self.assertEqual(result.status_code, 404)
        
    def test_JSON_format(self):
        response = self.client.get('StoreManager/api/v1/Products/',
                                   data="not a json format!")
        self.assertEqual(response.status_code, 404)
    
    


if __name__ == '__main__':
    unittest.main()
