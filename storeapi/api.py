# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:07:16 2018

@author: XaXa
"""


from flask import Flask
from flask import request
from flask import jsonify
from flask import abort
from flask import make_response


app = Flask(__name__)


products = [ ]
sales = [ ]


@app.route('/StoreManager/api/v1/', methods=['GET'])
def home():
    return ('Iwotokijikiji Store welcomes you'),200


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


@app.route('/StoreManager/api/v1/Products/All/', methods=['GET'])
def get_products():
    return jsonify({'products': products, 'message': "Showing all products"})


@app.route('/StoreManager/api/v1/Products/<productId>', methods=['GET'])
def get_product(productId):
    serial = [prod for prod in products if (prod == productId)]
    return jsonify({'prod': serial})


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

    products.append(create_prod)

    return jsonify(
            {"products": products, 'message': "success, added new product"}
            ), 201


@app.route('/StoreManager/api/v1/Sales/All', methods=['GET'])
def get_sales():
    return jsonify({'sales': sales, 'message': "Showing all sales records"})


@app.route('/StoreManager/api/v1/Sales/<salesId>', methods=['GET'])
def get_sale(salesId):
    usr = [new_record for new_record in sales if (new_record == salesId)]
    return jsonify({'new_record': usr, 'message': "Showing sale record by id"})


@app.route('/StoreManager/api/v1/Sales/Create', methods=['POST'])
def createnew_record():

    new_record = {
     'id': request.json['id'],
     'product': request.json['product'],
     'unit price': request.json['unit price'],
     'quantity': request.json['quantity'],
     'total price': request.json['total price'],
    }

    if not new_record['product']:
        return jsonify({'message': "Name can not be empty"}), 400

    if not new_record['id']:
        return jsonify({'message': "id is missing"}), 400

    if not new_record['unit price']:
        return jsonify({'message': "price is missing"}), 400

    if not new_record['quantity']:
        return jsonify({'message': "quantity is missing"}), 400

    if not new_record['total price']:
        return jsonify({'message': "total is missing"}), 400

    sales.append(new_record)

    return jsonify({'sales': sales, 'message': "created new sale "}), 201


app.config["DEBUG"] = True
