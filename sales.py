# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 01:22:54 2018

@author: XaXa
"""


from flask import Flask
from flask import jsonify

app = Flask(__name__)

sales_records = [

 {

  'id': 1110,

  'product': 'Rice',

  'unit price': '7,500 Ugx',

  'quantity': 5,

  'total price': '37,500 Ugx'

 },

 {

  'id': 1110,

  'product': 'T-shirt',

  'unit price': '10,000 Ugx',

  'quantity': 4,

  'total price': '40,000 Ugx'

 },

 {

  'id': 1110,

  'product': 'Mocassins',

  'unit price': '75,000 Ugx',

  'quantity': 2,

  'total price': '150,000 Ugx'

 },

 {

  'id': 1110,

  'product': 'Timbaland',

  'unit price': '150,000 Ugx',

  'quantity': 2,

  'total price': '300,000 Ugx'

 },

 {

  'id': 1110,

  'product': 'Maize flour',

  'unit price': '80,000 Ugx',

  'quantity': 10,

  'total price': '800,000 Ugx'

 },

 {

  'id': 1110,

  'product': 'Jean Trousers',

  'unit price': '30,000 Ugx',

  'quantity': 15,

  'total price': '450,000 Ugx'

 },

 ]


@app.route('/StoreManager/api/v1.0/sales', methods=['GET'])
def getAllSales():
    return jsonify({'sales_records': sales_records})


if __name__ == '__main__':
    app.run(debug=True)
