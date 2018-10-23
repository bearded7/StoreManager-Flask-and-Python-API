# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 23:15:38 2018

@author: XaXa
"""

import unittest
from unittest import TestCase

import flask
from flask import json, request

from endpoints.createproduct import app


class TestIwoto7(unittest.TestCase):
    def existNow(self):
        self.client = app.test_client()

    def test_route_admin_can_add_product_requires_login(self):
        feedback = self.client.get(
            'StoreManager/api/v1/Products/', follow_redirects=True)
        self.assertIn('Please log in to access this page', feedback.data)

    def test_admin_can_create_product(self):
        product = {
                 'id': request.json['id'],
                 'name': request.json['name'],
                 'price': request.json['price']
        }

        outcome = self.client.post('StoreManager/api/v1/Products/Add/',
                                   content_type='application/json',
                                   data=json.dumps(product))

        self.assertEqual(outcome.status_code, 404)
        self.assertIsNotNone(outcome)


if __name__ == '__main__':
    unittest.main()
