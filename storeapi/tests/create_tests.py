import unittest
import json
import requests 
from unittest import TestCase

def test_admin_and_attendant_can_get_products(self):
    res = self.client.get(
        'StoreManager/api/v1/GetAllProducts'
    )
    self.assertEqual(200, res.status_code)

    res = self.admin.get (
        'StoreManager/api/v1/GetAllProducts'
    )
    self.assertEqual(200, res.status_code)

def test_both_admin_attendant_can_get_specific_product(self):
    id = 110
    id = 111
    id = 112
    id = 113
    id = 114
    id = 115

    res = self.client.get(
        'StoreManager/api/v1/Products/%d' %id,
    )
    data = json.loads(res.data)
    print(data)
    print(res.status_code)
    self.assertEqual(200, res.status_code, msg = "product located")

def test_cannot_get_invalid_product_id(self):
    self.product_url = "http://localhost:5000/StoreManager/api/v1/Products/1"
    res = self.client.get(self.product_url)
    self.assertEqual(404, res.status_code)

def test_admin_can_get_all_sale_records(self):
    res = self.admin.get(
        'StoreManager/api/v1/GetAllSales'
    )
    self.assertEqual(200, res.status_code)

def test_route_get_all_sales_requires_login(self):
    res = self.admin.get(
        'StoreManager/api/v1/GetAllSales', follow_redirects=True)
    self.assertIn(b'Please log in to access this page', response.data)

def test_client_can_get_own_sale_records(self):
    id = 1110
    id = 1113
    id = 1115

    res = self.client.get(
        'StoreManager/api/v1/ProductsSales/%d' %id,
    )
    data = json.loads(res.data)
    print(data)
    print(res.status_code)
    self.assertEqual(200, res.status_code, msg = "Here is your sale record")

def test_route_get_own_sales_requires_login(self):
    res = self.client.get(
        'StoreManager/api/v1/Sales', follow_redirects=True)
    self.assertIn(b'Please log in to access this page', response.data)

def test_admin_can_add_product(self):
    res = self.admin.post(
        'StoreManager/api/v1/AddProducts'
    )
    self.assertEqual(200, res.status_code)

def test_route_admin_can_add_product_requires_login(self):
    res = self.admin.get(
        'StoreManager/api/v1/Products', follow_redirects=True)
    self.assertIn(b'Please log in to access this page', response.data)

def test_client_can_create_sales_records(self):
    res = self.client.post(
        'StoreManager/api/v1/CreateSales'
    )
    self.assertEqual(200, res.status_code)

def test_route_create_new_sales_records_requires_login(self):
    res = self.client.get(
        'StoreManager/api/v1/Sales', follow_redirects=True)
    self.assertIn(b'Please log in to access this page', response.data)

if __name__ == '__main__':
    unittest.main()