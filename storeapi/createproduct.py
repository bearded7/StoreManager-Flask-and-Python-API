# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 02:24:41 2018

@author: XaXa
"""


from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response


from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()


app = Flask(__name__)


@auth.get_password
def get_password(username):
    if username == 'admin':
        return 'python'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify(
        {'error': '''Unauthorized access
        Use
        Username: admin
        password: python
    '''}
    ), 401)


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


@app.route('/StoreManager/api/v1/Products/Add/', methods=['POST'])
@auth.login_required
def createProduct():

    details = {

     'id': request.json['id'],

     'name': request.json['name'],

     'price': request.json['price']

    }

    products.append(details)

    return jsonify(details)


if __name__ == '__main__':
    app.run(debug=True)
