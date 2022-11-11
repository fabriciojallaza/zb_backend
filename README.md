# Catalog System REST API

###### Zebrands Backend Test

A RESTful API for a catalog system to manage products. The API is built using Django, Django REST Framework, SQLite, AWS SES, Swagger, Redoc. 

This system has two main models: Product and User. A Product has a sku, name, price, brand, creation date, edition date and amount of visits. A User has a username, email, password and creation date.

There are three types of users: admin, non-admin and anonymous. Admins can create, edit and delete products and other admin/users. Non-admins can view products without incrementing visits field of a product. Anonymous users can only read products.

If a product is updated an email is sent to all admins with the proper information. And a track of the number of visits is kept for each product when an anonymous user views it, business reports could be obtained from this information.

## Installation & Run

### Install requirements for Linux
It requires Python 3.7 or higher

~~~bash
sudo apt update
sudo apt-get install python3-pip
sudo pip3 install virtualenv
sudo apt-get install git-all
sudo apt-get install sqlite3
~~~


### Clone the repository

~~~bash
# Mediante protocolo https
git clone https://github.com/fabriciojallaza/zb_backend.git

# Mediante protocolo ssh
git clone git@github.com:fabriciojallaza/zb_backend.git
~~~

### Create virtualenv

~~~bash
python3 -m virtualenv venv
~~~

### Activate virtualenv:

~~~bash
# For python >=3.10
source venv/local/bin/activate
# For python <3.10
source venv/bin/activate
~~~

### Install dependencies


#### Install requirements for virtualenv:

~~~bash
pip install -r requirements.txt
~~~

#### Introduce your own settings for email configuration in settings.py file:
The deployed version uses AWS SES service to send emails. You can use your own email service or use the default SMTP service provided by Django.

~~~python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your.host'
EMAIL_HOST_USER = 'your.user'
EMAIL_HOST_PASSWORD = 'your.password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
~~~

#### Initialize setup:
It creates an admin user and populates the database with some products.
~~~bash
python manage.py zb-setup
~~~

#### To Run Tests:

~~~bash
python manage.py test
~~~

#### Run server:

~~~bash
python manage.py runserver

# API Endpoint : http://127.0.0.1:8000
~~~

To login into the platform as admin, use the following credentials:

username: admin_user

password: admin_pass123

## Structure

```
.
├── catalog_system
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core
│   ├── management
│   │   └── __init__.py
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   └── zb-setup.py
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── products
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
├── user
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── utils
    └── email_handler.py

8 directories, 40 files
```

## API
Documentation for the API can be found under the following links:
* Swager UI: http://127.0.0.1:8000/docs/
* Redoc: http://127.0.0.1:8000/redoc/
* 
To Test the API follow the instructions in the end of this document.

### /v1/products/
* **GET**: List all products

### /v1/products/control/<int:product_id>/
* **GET**: Get product details
* **PUT**: Update product
* **PATCH**: Partial update product
* **DELETE**: Delete product

### /v1/products/create/
* **POST**: Create product

### /v1/products/:id/
* **GET**: Get product details as anonymous user

### /v1/user/
* **GET**: List all users

### /v1/user/authtoken/
* **POST**:  Log in with credentials and get a token

### /v1/user/manage/create/
* **POST**: Create a new user

### /v1/user/manage/:id/
* **GET**: Get user details
* **PUT**: Update user details
* **PATCH**: Update user details
* **DELETE**: Delete user

## Architecture Design
Django has a modular design that allows to create a scalable and maintainable architecture.

# Deployment
The API is deployed in AWS EC2 instance. The instance is configured to run the API using gunicorn and nginx. The API is served in the following endpoint: [Catalog System API Online - AWS EC2](http://ec2-3-93-152-219.compute-1.amazonaws.com:8000/)

To login into the platform and test the API or make it in the localhost, follow this link: [Catalog System Docs](http://ec2-3-93-152-219.compute-1.amazonaws.com:8000/docs/)

1. Click on the "Login" button
![Alt](/images/zp_api_docs.png "API Docs")
2. Introduce your credentials
![Alt](/images/login.png "Login")
3. Copy the token and go back to the API [Docs](http://ec2-3-93-152-219.compute-1.amazonaws.com:8000/docs/)
4. Click on the "Authorize" button and paste the token with the word "Token" before the token
![Alt](/images/token_auth.png "Authorize")
5. Now you can test the API