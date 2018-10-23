# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 23:15:38 2018

@author: XaXa
"""

import unittest
from unittest import TestCase
import flask
from flask import json
from flask import request
from endpoints.createproduct import app


class TestIwoto7(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add_product(self):
        product = {
                "id": 112,
                "name": "T-Shirt",
                "Price": "10,000 Ugx",
        }

        result = self.client.post('StoreManager/api/v1/Products/Add/',
                                  content_type='application/json',
                                  data=json.dumps(product)
                                  )

        self.assertEqual(result.status_code, 404)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
