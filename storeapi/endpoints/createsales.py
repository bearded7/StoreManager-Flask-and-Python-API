<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 03:23:53 2018

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
    if username == 'attendant':
        return 'python'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


sales = [

 {

  'id': '1110',

  'product': 'Rice',

  'unit price': '7,500 Ugx',

  'quantity': 5,

  'total price': '37,500 Ugx'

 },

 {

  'id': '1111',

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

  'id': '1113',

  'product': 'Timbaland',

  'unit price': '150,000 Ugx',

  'quantity': 2,

  'total price': '300,000 Ugx'

 },

 {

  'id': '1114',

  'product': 'Maize flour',

  'unit price': '80,000 Ugx',

  'quantity': 10,

  'total price': '800,000 Ugx'

 },

 {

  'id': '1115',

  'product': 'Jean Trousers',

  'unit price': '30,000 Ugx',

  'quantity': 15,

  'total price': '450,000 Ugx'

 },

 ],

saless = [{}],


@app.route('/StoreManager/api/v1/CreateSales', methods=['POST'])
@auth.login_required
def createSales():

    details = {

     'id': request.json['id'],

     'product': request.json['product'],

     'unit price': request.json['unit price'],

     'quantity': request.json['quantity'],

     'total price': request.json['total price']

    }

    saless.append(details)

    return jsonify(details)

    


if __name__ == '__main__':
    app.run(debug=True)
=======
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 03:23:53 2018

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
    if username == 'attendant':
        return 'python'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


sales = [

 {

  'id': '1110',

  'product': 'Rice',

  'unit price': '7,500 Ugx',

  'quantity': 5,

  'total price': '37,500 Ugx'

 },

 {

  'id': '1111',

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

  'id': '1113',

  'product': 'Timbaland',

  'unit price': '150,000 Ugx',

  'quantity': 2,

  'total price': '300,000 Ugx'

 },

 {

  'id': '1114',

  'product': 'Maize flour',

  'unit price': '80,000 Ugx',

  'quantity': 10,

  'total price': '800,000 Ugx'

 },

 {

  'id': '1115',

  'product': 'Jean Trousers',

  'unit price': '30,000 Ugx',

  'quantity': 15,

  'total price': '450,000 Ugx'

 },

 ],

saless = [{}],


@app.route('/StoreManager/api/v1/CreateSales', methods=['POST'])
@auth.login_required
def createSales():

    details = {

     'id': request.json['id'],

     'product': request.json['product'],

     'unit price': request.json['unit price'],

     'quantity': request.json['quantity'],

     'total price': request.json['total price']

    }

    saless.append(details)

    return jsonify(details)

    


if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> a6d76adb4566707dd7bcefc769187e4f0d468d63
