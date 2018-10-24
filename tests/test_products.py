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


class TestIwoto3(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        
    def test_get_all_products(self):
        result = self.client.get('StoreManager/api/v1/Products/All/')
        self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
    unittest.main()
