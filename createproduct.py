# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 02:24:41 2018

@author: XaXa
"""


from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

products = [
 {

  'id': 110,

  'name': 'Rice',

  'Price': '7,500 Ugx'

 },

 {

  'id': 111,

  'name': 'Mocassins',

  'Price': '75,000 Ugx'

 },

 {

  'id': 112,

  'name': 'T-Shirt',

  'Price': '10,000 Ugx'

 },

 {

  'id': 113,

  'name': 'Timbaland',

  'Price': '150,000 Ugx'

 },

 {

  'id': 114,

  'name': 'Maize Flour',

  'Price': '80,000 Ugx'

 },

 {

  'id': 115,

  'name': 'Jean Trousers',

  'Price': '30,000 Ugx'

 }

 ]


@app.route('/StoreManager/api/v1.0/products/add', methods=['POST'])
def createProduct():

    details = {

     'id': request.json['id'],

     'name': request.json['name'],

     'title': request.json['title']

    }

    products.append(details)

    return jsonify(details)


if __name__ == '__main__':
    app.run(debug=True)
