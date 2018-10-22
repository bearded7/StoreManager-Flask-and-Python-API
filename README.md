# StoreManager-Flask-and-Python-API
A CRUD web API with GET and POST functionalities 

[![Maintainability](https://api.codeclimate.com/v1/badges/de3d25a8dafaada7833c/maintainability)]

[![Coverage Status](https://coveralls.io/repos/github/bearded7/StoreManager-Flask-and-Python-API/badge.svg?branch=develop)]

[![Build Status](https://travis-ci.org/github/bearded7/StoreManager-Flask-and-Python-API.png?branch=develop)]




[Flask](http://flask.pocoo.org/) is a micro web framework powered by Python. Its API is fairly small, making it easy to learn and simple to use. But don't let this fool you, as it's powerful enough to support enterprise-level applications handling large amounts of traffic. You can start small with an app contained entirely in one file, then slowly scale up to multiple files and folders in a well-structured manner as your site becomes more and more complex.

1. The Plan

In this exercise, we will create an in-memory JSON Database to store and manipulate a simple store database and develop RESTful APIs to perform CRUD operations using GET and POST methods. We will develop the below APIs
i) GET  /StoreManager/api/v1/Products/All     - Retrieve all products in the database
ii) GET /StoreManager/api/v1/Products/<id>      - Retrieve the details of given product using Id
iii) GET  /StoreManager/api/v1/Sales/All            - Retrieve all sales records in the database
iv) GET /StoreManager/api/v1/Sales/<id>         - Retrieve the details of given product using Id
v) POST  /StoreManager/api/v1/Products/Add     - update product in the database
vi) POST /StoreManager/api/v1/Sales/Sales/Create       - update sales record in the database

2. Conditions to be met

- The home page of the API is /
- To access all products: /StoreManager/api/v1/Products/All
- To access product by id: /StoreManager/api/v1/Products/<productId>
- To access All sales (admin only, username is admin, password is python) /StoreManager/api/v1/Sales/All
- To access specific sale record (attendant only, username is attendant, password: python) /StoreManager/api/v1/Sales/<salesId>
- To create a product(admin only): /StoreManager/api/v1/Products/Add
- To create a sale record (attendant only): /StoreManager/api/v1/Sales/Create


3. Installation of Flask

To install flask framework, please refer the official website [1]. If you have pip installed in your Python environment, please follow this step.

$ pip install Flask

If you don't have pip, please download the flask from http://pypi.python.org/packages/source/F/Flask/Flask-0.10.1.tar.gz and execute the setup.py

4. 





