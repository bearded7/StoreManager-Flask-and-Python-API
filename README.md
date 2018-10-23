# StoreManager-Flask-and-Python-API
A CRUD web API with GET and POST functionalities 

[![Coverage Status](https://coveralls.io/repos/github/bearded7/StoreManager-Flask-and-Python-API/badge.svg?branch=develop)](https://coveralls.io/github/bearded7/StoreManager-Flask-and-Python-API?branch=develop)
[![Build Status](https://travis-ci.org/bearded7/StoreManager-Flask-and-Python-API.svg?branch=develop)](https://travis-ci.org/bearded7/StoreManager-Flask-and-Python-API?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/de3d25a8dafaada7833c/maintainability)](https://codeclimate.com/github/bearded7/StoreManager-Flask-and-Python-API/maintainability)


[Flask](http://flask.pocoo.org/) is a micro web framework powered by Python. Its API is fairly small, making it easy to learn and simple to use. That's not all as it's powerful enough to support enterprise-level applications handling large amounts of traffic. I have started small with an app contained entirely in one file, then I intend to slowly scale up to multiple files and folders in a well-structured manner as my site becomes more and more complex.


1. Conditions to be met for this challenge

- The home page of the API is /
- To access all products: /StoreManager/api/v1/Products/All
- To access product by id: /StoreManager/api/v1/Products/<productId>
- To access All sales (admin only, username is admin, password is python) /StoreManager/api/v1/Sales/All
- To access specific sale record (attendant only, username is attendant, password: python) /StoreManager/api/v1/Sales/<salesId>
- To create a product(admin only): /StoreManager/api/v1/Products/Add
- To create a sale record (attendant only): /StoreManager/api/v1/Sales/Create