<<<<<<< HEAD
from flask import Flask
=======
import Flask 
>>>>>>> a6d76adb4566707dd7bcefc769187e4f0d468d63
from storeapi.endpoints.app import sales
from storeapi.endpoints.app import products
from storeapi.endpoints.app import new_product
from storeapi.endpoints.app import new_sales


app = Flask(__name__) 
api = app(app)

<<<<<<< HEAD
api.add_resource(Products, 'StoreManger/api/v1/Product/<int:product_id>')
api.add_resource(GetAllProducts, 'StoreManager/api/v1/GetAllProducts')
api.add_resource(AddProducts, 'StoreManager/api/v1/AddProducts')

api.add_resource(Sales, 'StoreManager/api/v1/Sale/<int:sale_id>')
api.add_resource(GetAllSales, 'StoreManager/api/v1/GetAllSales')
=======
api.add_resource(Product, 'StoreManger/api/v1/Product/<int:product_id>')
api.add_resource(ProductList, 'StoreManager/api/v1/GetAllProducts')
api.add_resource(CreateProduct, 'StoreManager/api/v1/AddProducts')

api.add_resource(Sale, '/api/v1/sale/<int:sale_id>')
api.add_resource(Sales, '/api/v1/sales')
>>>>>>> a6d76adb4566707dd7bcefc769187e4f0d468d63
api.add_resource(CreateSales, 'StoreManager/api/v1/CreateSales')
