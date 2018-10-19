# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:07:16 2018

@author: XaXa
"""


from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request

from flask_httpauth import HTTPBasicAuth
Auth = HTTPBasicAuth()


@Auth.get_password
def get_password(username):
    if username == 'admin':
        return 'python'
    return None


@Auth.error_handler
def unauthorizd():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


App = Flask(__name__)


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

     'Price': '80,000 Ugx',

    },

    {

     'id': '115',

     'name': 'Jean Trousers',

     'Price': '30,000 Ugx',

    }

        ]

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

     'id': '1112',

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

        ]


@App.route('/StoreManager/v1/GetAllProducts', methods=['GET'])
def get_products():
    return jsonify({'products': products})


@App.route('/StoreManager/v1/Products/<productId>', methods=['GET'])
def get_product(productId):
    usr = [prod for prod in products if (prod['id'] == productId)]
    return jsonify({'prod': usr})


@App.route('/StoreManager/v1/GetAllSales', methods=['GET'])
@Auth.login_required
def get_sales():
    return jsonify({'sales': sales})


@App.route('/StoreManager/v1/Sales/<salesId>', methods=['GET'])
@Auth.login_required
def get_sale(salesId):
    usr = [rec for rec in sales if (rec['id'] == salesId)]
    return jsonify({'rec': usr})


@App.route('/StoreManager/v1/AddProducts', methods=['POST'])
@Auth.login_required
def create_product():

    dat = {

        'id': request.json['id'],

        'name': request.json['name'],

        'price': request.json['price'],

    }

    products.append(dat)

    return jsonify(dat)


@App.route('/StoreManager/v1/CreateSales', methods=['POST'])
def createRec():

    dat = {
     'id': request.json['id'],
     'product': request.json['product'],
     'unit price': request.json['unit price'],
     'quantity': request.json['quantity'],
     'total price': request.json['total price'],
    }

    sales.append(dat)

    return jsonify(dat)


if __name__ == '__main__':
    App.run(debug=True)