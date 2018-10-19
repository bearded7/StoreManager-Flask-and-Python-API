# StoreManager-Flask-and-Python-API
A CRUD web API that with GET and POST functionalities 

[github pages](https://bearded7.github.io/Store-Manager/UI/) 

[![Maintainability](https://api.codeclimate.com/v1/badges/de3d25a8dafaada7833c/maintainability)]
(https://codeclimate.com/github/bearded7/StoreManager-Flask-and-Python-API/maintainability)

[![Coverage Status](https://coveralls.io/repos/github/bearded7/StoreManager-Flask-and-Python-API/badge.png)]
(https://coveralls.io/github/bearded7/StoreManager-Flask-and-Python-API)

[![Build Status](https://travis-ci.org/github/bearded7/StoreManager-Flask-and-Python-API.svg?branch=develop)]
(https://github/bearded7/StoreManager-Flask-and-Python-API)

[Flask](http://flask.pocoo.org/) is a micro web framework powered by Python. Its API is fairly small, making it easy to learn and simple to use. But don't let this fool you, as it's powerful enough to support enterprise-level applications handling large amounts of traffic. You can start small with an app contained entirely in one file, then slowly scale up to multiple files and folders in a well-structured manner as your site becomes more and more complex.

1. The Plan

In this exercise, we will create an in-memory JSON DB to store and manipulate a simple employee database and develop RESTful APIs to perform CRUD operations using GET and POST methods. We will develop the below APIs
i) GET  /StoreManager/api/v1/GetAllProducts     - Retrieve all products in the database
ii) GET /StoreManager/api/v1/Products/<id>      - Retrieve the details of given product using Id
iii) GET  /StoreManager/api/v1/Sales            - Retrieve all sales records in the database
iv) GET /StoreManager/api/v1/Sales/<id>         - Retrieve the details of given product using Id
v) POST  /StoreManager/api/v1/Products/AddProduct     - update product in the database
vi) POST /StoreManager/api/v1/Sales/CreateSales       - update sales record in the database

2. Conditions to 
