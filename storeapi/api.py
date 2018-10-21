# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:07:16 2018

@author: XaXa
"""


from flask import Flask, request, jsonify, abort, make_response


app = Flask(__name__)
app.config["DEBUG"] = True

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


new_product = [{}],
new_sales = [{}],


@app.route('/', methods=['GET'])
def home():
    return ('Welcome to Iwotokijikiji Store Manager'),200


@app.errorhandler(405)
def url_not_found(error):
    return jsonify({'message': 'Requested method not allowed'}), 405


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'message': 'page not found, check the url'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'internal server error'}), 500


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'product not found'}), 404)


@app.route('/StoreManager/api/v1/Products/All', methods=['GET'])
def get_products():
    return jsonify({'products': products})


@app.route('/StoreManager/api/v1/Products/<productId>', methods=['GET'])
def get_product(productId):
    usr = [prod for prod in products if (prod['id'] == productId)]
    return jsonify({'prod': usr})


@app.route('/StoreManager/api/v1/Products/Add', methods=['POST'])
def create_prod():

    create_prod = {
     'id': request.json['id'] + 1,
     'product_name': request.json['product_name'],
     'unit price': request.json['unit price'],
     'quantity': request.json['quantity'],
     'total price': request.json['total price'],
    }

    if not create_prod['product_name']:
        return jsonify({'message': "Name can not be empty"}), 400

    if not create_prod['id']:
        return jsonify({'message': "id is missing"}), 400

    if not create_prod['unit price']:
        return jsonify({'message': "price is missing"}), 400

    if not create_prod['quantity']:
        return jsonify({'message': "quantity is missing"}), 400

    if not create_prod['total price']:
        return jsonify({'message': "total is missing"}), 400

    new_product.append(create_prod)

    return jsonify(
            {new_product: "craete_prod", 'message': "successfully added"}
            ), 201


@app.route('/StoreManager/api/v1/Sales/All', methods=['GET'])
def get_sales():
    return jsonify({'sales': sales})


@app.route('/StoreManager/api/v1/Sales/<salesId>', methods=['GET'])
def get_sale(salesId):
    usr = [rec for rec in sales if (rec['id'] == salesId)]
    return jsonify({'rec': usr})


@app.route('/StoreManager/api/v1/Sales/Create', methods=['POST'])
def createRec():

    rec = {
     'id': request.json['id'],
     'product': request.json['product'],
     'unit price': request.json['unit price'],
     'quantity': request.json['quantity'],
     'total price': request.json['total price'],
    }

    if not rec['product']:
        return jsonify({'message': "Name can not be empty"}), 400

    if not rec['id']:
        return jsonify({'message': "id is missing"}), 400

    if not rec['unit price']:
        return jsonify({'message': "price is missing"}), 400

    if not rec['quantity']:
        return jsonify({'message': "quantity is missing"}), 400

    if not rec['total price']:
        return jsonify({'message': "total is missing"}), 400

    new_sales.append(rec)

    return jsonify({new_sales: "rec", 'message': "successfully added"}), 201


                                                                                                                                                                                                                                                                                                                                    

