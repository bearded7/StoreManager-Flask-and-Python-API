# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 03:23:53 2018

@author: XaXa
"""


from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

sales = [

 {

  'id': 1110,

  'product': 'Rice',

  'unit price': '7,500 Ugx',

  'quantity': 5,

  'total price': '37,500 Ugx'

 },

 {

  'id': 1111,

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

  'id': 1113,

  'product': 'Timbaland',

  'unit price': '150,000 Ugx',

  'quantity': 2,

  'total price': '300,000 Ugx'

 },

 {

  'id': 1114,

  'product': 'Maize flour',

  'unit price': '80,000 Ugx',

  'quantity': 10,

  'total price': '800,000 Ugx'

 },

 {

  'id': 1115,

  'product': 'Jean Trousers',

  'unit price': '30,000 Ugx',

  'quantity': 15,

  'total price': '450,000 Ugx'

 },

 ]


@app.route('/StoreManager/api/v1.0/sales/add', methods=['POST'])
def createSales():

    details = {

     'id': request.json['id'],

     'product': request.json['product'],

     'unit price': request.json['unit price'],

     'quantity': request.json['quantity'],

     'total price': request.json['total price']

    }

    sales.append(details)

    return jsonify(details)


if __name__ == '__main__':
    app.run(debug=True)
