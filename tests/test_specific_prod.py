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

    def test_fetch_unavailable_product(self):
        result = self.client.get('StoreManager/api/v1/Products/')
        self.assertEqual(result.status_code, 404)
        
    def test_JSON_format(self):
        response = self.client.get('StoreManager/api/v1/Products/',
                                   data="not a json format!")
        self.assertEqual(response.status_code, 404)
    
    


if __name__ == '__main__':
    unittest.main()
