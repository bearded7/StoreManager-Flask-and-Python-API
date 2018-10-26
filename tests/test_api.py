# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:07:16 2018

@author: XaXa
"""


import flask
import unittest
from flask import json
from storeapi.api import app


class Testclient1(unittest.TestCase):
    products = {
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

    sales = {
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
    }

    new_product = {},
    new_sale = {}


    def setUp(self):
        self.client = app.test_client()

    def test_home_base(self):
        response = self.client.get('/StoreManager/api/v1/',
        content_type='apllication/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.status_code, 500)

    def test_get_all_rpoduct_by_id(self):
        self.client.get('StoreManager/api/v1/Products/All/',
                        content_type= 'application/json',
                        data= json.dumps(self.products)
                        )
        result= self.client.get('StoreManager/api/v1/Products/All/')
        print(result)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data.decode()), {'200': [self.products]})
        self.client.delete('StoreManager/api/v1/Products/113')

    def test_get_all_product(self):
        result = self.client.get('StoreManager/api/v1/Products/113',
        content_type='response.status'
        )
        self.assertEqual(result.status_code, 200)
        self.assertFalse(result.status, 500)

    def test_get_unavailable_product(self):
        result = self.client.get('StoreManager/api/v1/Products/')
        self.assertEqual(result.status_code, 404)

    def test_add_product(self):
        add_product = self.client.post(
            'StoreManager/api/v1/Products/Add/',
            content_type='application/json',
            data=json.dumps(self.new_product))
                                  
        self.assertEqual(add_product.status_code, 201)
        self.assertEqual(json.loads(add_product.data.decode()), {'201': 'New product added'})
        self.client.delete('StoreManager/api/v1/Products/115')

    def test_get_all_sales_recs(self):
        result = self.client.get('StoreManager/api/v1/Sales/All/')
        self.assertEqual(result.status_code, 404)

    def test_get_specific_sale(self):
        result = self.client.get('StoreManager/api/v1/Sales/1114')
        self.assertEqual(result.status_code, 200)

    def test_unavailable_sales_fetch(self):
        result = self.client.get('StoreManager/api/v1/Sales/')
        self.assertEqual(result.status_code, 404)

    def test_add_sale(self):
        new_sale = {
            "id": 116,
            "product_name": "maize",
            "unit price": "12,000 Ugx per Kg",
            "quantity": "1 KG",
            "total price": "12,000 Ugx",
        }

        result = self.client.post(
            'StoreManager/api/v1/Sales/Create/',
            content_type='application/json',
            data=json.dumps(new_sale))

        self.assertEqual(result.status_code, 404)
        self.assertIsNotNone(result)
    
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode()), {"Hello Admin":"Welcome to ManagerStore"})
    
    def test_add_product_successfully(self):
        post_product = self.client.post('/api/v1/products',
                                        content_type='application/json',
                                        data = json.dumps(self.products)
                                        )
        self.assertEqual(post_product.status_code, 201)
        self.assertEqual(json.loads(post_product.data.decode()), {'201': 'Product successfully added'})
        self.client.delete('/api/v1/products/1')
   
    def test_list_all_products(self):
        self.client.post('/StoreManager/api/v1/Products/All',
                        content_type='application/json',
                        data=json.dumps(self.new_product)
                        )
        result = self.client.get('/api/v1/products')
        print(result)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data.decode()), {'200': [self.products]})
        self.client.delete('/api/v1/products/1'),


if __name__ == '__main__':
    unittest.main()
