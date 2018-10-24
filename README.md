# StoreManager-Flask-and-Python-API
A CRUD web API with GET and POST functionalities 

[![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)
[![Build Status](https://travis-ci.org/bearded7/StoreManager-Flask-and-Python-API.svg?branch=develop)](https://travis-ci.org/bearded7/StoreManager-Flask-and-Python-API?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/de3d25a8dafaada7833c/maintainability)](https://codeclimate.com/github/bearded7/StoreManager-Flask-and-Python-API/maintainability)

REST APIs are in constant use in the life of a software developer. To make it as a software developer one must master how to build well designed and  functional APIs.
The Project is my First trial at craeting a RESTful Flask and Python Web API.
It is a culmination of lots of hours consulting and researching.

# Prerequisites

 To install [Flask](http://flask.pocoo.org/) please refer the official website. If you have pip installled in your Python environment, please follow this steps;
```
$ pip install Flask
```
- After pip installs, we are raedy to begin

1. Conditions to be met for this challenge

- The home page of the API is /StoreManager/api/v1/
- To access all products: /StoreManager/api/v1/Products/All
- To access product by id: /StoreManager/api/v1/Products/<productId>
- To access All sales (admin only, username is admin, password is python) /StoreManager/api/v1/Sales/All
- To access specific sale record (attendant only, username is attendant, password: python) /StoreManager/api/v1/Sales/<salesId>
- To create a product(admin only): /StoreManager/api/v1/Products/Add
- To create a sale record (attendant only): /StoreManager/api/v1/Sales/Create

# Creating a Hello World Web Server

- First, we create a web server, create a dictionary to hold a JSON objects for a couple of employee records and then we add RESTful APIs for each supported operations. Please look at the below program, which creates a web server. Save the below program into hello.py and execute it.

```

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run()
```
- Execute the above program and you will see that you web server is ready to service you.
And repeat
- Now you can open your web browser and check your web server. The server is available in the URL http://localhost:5000/. If you are familiar with cUrl execute the below to check the status.

```
$ curl -i http://localhost:5000/
```

# Develop the RESTful Services

- To develop the restful services for the planned objective, let's create an in-memory database in python using the dictionary data type.

GET
- We have created two products in the dictionary. Now let's write a code to retrieve them using web services. As per our plan, we need two implementations one is to retrieve all the products and another one to retrieve the specific product with the given id.

GET SPECIFIC
- Now we develop the rest service to get a product with a given id.

POST
- POST method is used to create a new employee inside the database.

- This is a very basic web services we have developed.  I hope this helps to understand basics of RESTful Web Services development.


# Tests

You can now run the tests from the terminal using pytest
```
pytest api.py
```
You can also run tests with coverage by running this command in the terminal
```
nosetests --with-coverage --cover-package=app
```

# Deployment

- Install Heroku CLI
- Set up git (If you don't already have it)
- Create a Heroku App  command 

```
$ heroku apps:create flask-microblog
Creating flask-microblog... done
http://flask-microblog.herokuapp.com/ | https://git.heroku.com/flask-microblog.git
```

-Create a Procfile with contents 

```
web: flask db upgrade; flask translate compile; gunicorn microblog:app
```

- Create a requirements.txt file with command 

```
 pip>freeze requirements.txt
```

- Deploy to Heroku with command  

``` 
git push heroku master
```

# Built With

 Python, Flask


# Versioning

We use the format v1, for this project. only whole numbers allowed. 

# Authors

* **Oriba Douglas** - *Initial work* 


# License

This project is open licensed.

# Acknowledgments

* Saravanan Subramanian https://techietweak.wordpress.com/


