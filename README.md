# Instalacion en Linux

## Instalar virtualenv

~~~bash
sudo apt-get install python3-pip
sudo pip3 install virtualenv
~~~

## Instalar sqlite

~~~bash
sudo apt-get install sqlite3
~~~

## Clonar repo

~~~bash
# Mediante protocolo https
git clone https://github.com/fabriciojallaza/zb_backend.git

# Mediante protocolo ssh
git clone git@github.com:fabriciojallaza/zb_backend.git
~~~

## Creamos en entorno virtual

~~~bash
python3 -m virtualenv venv
~~~

## Instalación de dependencias

### Activamos el virtualenv:

~~~bash
source venv/local/bin/activate
~~~

### Instalamos los requerimientos

~~~bash
pip install -r requirements.txt
~~~

### Corremos el Proyecto:

~~~bash
python manage.py runserver
~~~

## Working tree

~~~bash
.
├── catalog_system
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_user_email.py
│   │   ├── 0003_alter_user_email.py
│   │   ├── 0004_user_is_staff.py
│   │   ├── 0005_auto_20221110_0933.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-310.pyc
│   │       ├── 0002_alter_user_email.cpython-310.pyc
│   │       ├── 0003_alter_user_email.cpython-310.pyc
│   │       ├── 0004_user_is_staff.cpython-310.pyc
│   │       ├── 0005_auto_20221110_0933.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   └── tests.cpython-310.pyc
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
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── serializers.cpython-310.pyc
│   │   ├── tests.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── __pycache__
│   └── manage.cpython-310.pyc
├── README.md
├── requirements.txt
├── user
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── serializers.cpython-310.pyc
│   │   ├── tests.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── utils
    ├── email_handler.py
    └── __pycache__
        └── email_handler.cpython-310.pyc

17 directories, 77 files
~~~