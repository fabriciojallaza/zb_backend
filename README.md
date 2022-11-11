# Linux Installation

## Install virtualenv

~~~bash
sudo apt-get install python3-pip
sudo pip3 install virtualenv
~~~

## Install sqlite

~~~bash
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

### Install requirements:

~~~bash
pip install -r requirements.txt
~~~

### Initialize setup:

~~~bash
python manage.py zb-setup
~~~

### Run server:

~~~bash
python manage.py runserver
~~~

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

