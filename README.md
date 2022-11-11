# Instalacion en Linux
## Instalar virtualenv
sudo apt-get install python3-pip
sudo pip3 install virtualenv
## Instalar sqlite
sudo apt-get install sqlite3
## Clonar repo
git clone 
## Creamos en entorno virtual
python3 -m virtualenv venv
## Instalación de dependencias
### Activamos el virtualenv:
source venv/local/bin/activate
### Instalamos los requerimientos
pip install -r requirements.txt
### Corremos el Projecto:
python manage.py runserver