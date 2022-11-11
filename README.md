# Linux Installation

## Install requirements for Linux

~~~bash
sudo apt update
sudo apt-get install python3-pip
sudo pip3 install virtualenv
sudo apt-get install git-all
sudo apt-get install sqlite3
~~~


## Clone the repository

~~~bash
# Mediante protocolo https
git clone https://github.com/fabriciojallaza/zb_backend.git

# Mediante protocolo ssh
git clone git@github.com:fabriciojallaza/zb_backend.git
~~~

## Create virtualenv

~~~bash
python3 -m virtualenv venv
~~~

## Install dependencies

### Activate virtualenv:

~~~bash
source venv/local/bin/activate
~~~

### Install requirements for virtualenv:

~~~bash
pip install -r requirements.txt
~~~

### Introduce your own settings for email configuration in settings.py file:

~~~python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your.host'
EMAIL_HOST_USER = 'your.user'
EMAIL_HOST_PASSWORD = 'your.password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
~~~

### Initialize setup:

~~~bash
python manage.py zb-setup
~~~

### Run server:

~~~bash
python manage.py runserver
~~~

### To Run Tests:

~~~bash
python manage.py test
~~~

To login into the platform as admin, use the following credentials:

username: admin_user

password: admin_pass123

## Working tree

~~~bash
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
│   │   ├── 0002_alter_user_email.py
│   │   ├── 0003_alter_user_email.py
│   │   ├── 0004_user_is_staff.py
│   │   ├── 0005_auto_20221110_0933.py
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

