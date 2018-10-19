from flask import Flask, request, jsonify, abort, make_response


app = Flask(__name__)
app.config["DEBUG"] = True

products = []
sales = []


@app.route('/', methods=['GET'])
def home():
    return ('Welcome to Store Manager'),200


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


@app.route('/api/v2/resources/product/', methods=['POST'])
def create_product():
    product = {
        'id': request.json['id'] + 1,
        'product_name': request.json['product_name'],
        'price': request.json['price'],
        'quantity': request.json['quantity'],
        'category': request.json['category'],
    }

    if not product['product_name']:
        return jsonify({'message': "Name can not be empty"}), 400

    if not product['id']:
        return jsonify({'message':"id is missing"}), 400

    if not product['price']:
        return jsonify({'message':"price is missing"}),400

    if not product['quantity']:
        return jsonify({'message':"quantity is missing"}), 400

    if not product['category']:
        return jsonify({'message':"category is missing"}),400

    data = products.append(product)
    return jsonify({'data': products, 'message': "succesfully added"}), 201


@app.route('/api/v2/resources/products/all', methods=['GET'])
def products_all():
    return jsonify(products)


@app.route('/api/v2/resources/products/<pk>/', methods=['GET'])
def products_id(pk):
    try:
        int(pk)
    except:
        return jsonify({"error": "id input should be an integer"})

    for dict in products:
        if dict['id'] == int(pk):
            return jsonify(dict)

    else:
        return jsonify({"message": "The product with that id was not found"})


@app.route('/api/v2/resources/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):

    product = [product for product in products if int(
        product['id']) == int(product_id)]
    product[0]['name'] = request.json.get('name')
    product[0]['category'] = request.json.get('category')
    if len(product) == 0:
        abort(404)
    if not product[0]['name']:
        abort(400)

    return jsonify({'data': product, 'message': "succesfully updated"}), 200


@app.route('/api/v2/resources/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = [product for product in products if int(
        product['id']) == int(product_id)]
    if len(product) == 0:
        abort(404)
    products.remove(product[0])
    return jsonify({'message': "succesfully deleted"})

@app.route('/api/v2/resources/sale/', methods=['POST'])
def create_sales():
    sale = {
        'id': request.json['id'] + 1,
        'sales_name': request.json['sales_name'],
        'price': request.json['price'],
        'quantity': request.json['quantity'],
        'category': request.json['category'],
        'total':request.json['total']
    }

    if not sale['sales_name']:
        return jsonify({'message': "Name can not be empty"}), 400

    if not sale['id']:
        return jsonify({'message':"id is missing"}), 400

    if not sale['price']:
        return jsonify({'message':"price is missing"}),400

    if not sale['quantity']:
        return jsonify({'message':"quantity is missing"}), 400

    if not sale['category']:
        return jsonify({'message':"category is missing"}),400

    if not sale['total']:
        return jsonify({'message': "total is missing"}), 400
    
    data = sales.append(sale)
    return jsonify({'data': sales, 'message': "succesfully added"}), 201


@app.route('/api/v2/resources/sales/all', methods=['GET'])
def sales_all():
    return jsonify(sales)


@app.route('/api/v2/resources/sales/<pk>/', methods=['GET'])
def sales_id(pk):
    try:
        int(pk)
    except:
        return jsonify({"error": "id input should be an integer"})

    for dict in sales:
        if dict['id'] == int(pk):
            return jsonify(dict)

    else:
        return jsonify({"message": "The sales with that id was not found"})

                                                                                                                                                                                                                                                                                                                                    



