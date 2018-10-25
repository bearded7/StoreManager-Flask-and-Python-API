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

    def test_attendant_cannot_add_product(self):
        """Tests that the attendant cannot add a product"""
        with app.app_context():
            #  Add a new product
            response = self.client.post(
                "/api/v1/products",
                data=dict(
                    name="Laptop Bag",
                    price=150000
                ),
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Authorization": self.access_token_
                }
            )
            self.assertEqual(
                json.loads(response.data)["msg"], "Admin previlidges required")

    def test_attendant_cannot_edit_product(self):
        """Tests that the attendant cannot edit a product"""
        with app.app_context():
            product_changes = dict(
                product_id="539c3032",
                name="Sugar",
                price=10000,
                min_qty=25
            )
            res = self.client.post(
                "/api/v1/products/edit/{}".format("539c3032"), 
                data=product_changes,
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Authorization": self.access_token_
                }
            )
            self.assertEqual(json.loads(res.data)[
                "msg"], "Admin previlidges required")
        

    def test_attendant_cannot_delete_product(self):
        """Tests that the attendant cannot delete a product"""
        with app.app_context():
            res = self.client.delete(
                "/api/v1/products/delete/{}".format("055ad1fd"),
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Authorization": self.access_token_
                }
            )
            self.assertEqual(json.loads(res.data)[
                             "msg"], "Admin previlidges required")



if __name__ == '__main__':
    unittest.main()
