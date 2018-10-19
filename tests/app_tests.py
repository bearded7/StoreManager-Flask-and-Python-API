import unittest

from flask import Flask, json

from storeapi.base import app


class TestStore(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_base_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_product(self):
        product = {
            "product_name": "Rice",
            "price": "9,500",
            "quantity": 6,
            "category": "Cereals"
        }

        result = self.client.post('/api/v2/resources/product/',
                                  content_type='application/json',
                                  data=json.dumps(product)
                                  )

        self.assertEqual(result.status_code, 201)
        self.assertIsNotNone(result)

    def test_get_all_products(self):
        result = self.client.get('/api/v2/resources/products/all')
        self.assertEqual(result.status_code, 200)

    def test_add_single_product(self):
        product = {
            "product_name": "Rice",
            "price": "9,500",
            "quantity": 6,
            "category": "Cereals"
        }

        result = self.client.post('/api/v2/resources/product/', content_type='application/json',
                                  data=json.dumps(product)
                                  )

        self.assertEqual(result.status_code, 201)

    def test_unavailable_fetch(self):
        result = self.client.get('/api/v2/resources/products/')
        self.assertEqual(result.status_code, 404)

        result = self.client.post('/api/v2/resources/order/',
                                  content_type='application/json',
                                  data=json.dumps(sale)
                                  )

        self.assertEqual(result.status_code, 404)
        self.assertIsNotNone(result)

    def test_get_all_sales(self):
        result = self.client.get('/api/v2/resources/sale/all')
        self.assertEqual(result.status_code, 404)

    def test_add_single_sale(self):
        sale = {
            "id": 1117,
            "sales_name": "Whiskey",
            "price": "30,000",
            "quantity": 10,
            "category": "Drinks",
            "total": "300,000"
        }

        result = self.client.post('/api/v2/resources/sale/', content_type='application/json',
                                  data=json.dumps(sale)
                                  )

        self.assertEqual(result.status_code, 201)
