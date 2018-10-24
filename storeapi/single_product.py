# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 00:04:12 2018

@author: XaXa
"""


from flask import Flask
from flask import jsonify

app = Flask(__name__)

products = [
 {

  'id': '110',

  'name': 'Rice',

  'Price': '7,500 Ugx'

 },

 {

  'id': '111',

  'name': 'Mocassins',

  'Price': '75,000 Ugx'

 },

 {

  'id': '112',

  'name': 'T-Shirt',

  'Price': '10,000 Ugx'

 },

 {

  'id': '113',

  'name': 'Timbaland',

  'Price': '150,000 Ugx'

 },

 {

  'id': '114',

  'name': 'Maize Flour',

  'Price': '80,000 Ugx'

 },

 {

  'id': '115',

  'name': 'Jean Trousers',

  'Price': '30,000 Ugx'

 }

 ]


@app.route('/StoreManager/v1/Products/<productId>', methods=['GET'])
def getProduct(productId):
    serial = [prod for prod in products if (prod['id'] == productId)]
    return jsonify({'prod': serial})


if __name__ == '__main__':
    app.run(debug=True)
