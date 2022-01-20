# InventoryManagement

The project is a basic Inventory Management system using the Django framework. A server will be run as a local host on the machine in use.

## Installation Steps

To effectively use this project, Python version 3.9.10 and Django version 4.0.1 were used. 

- First, to download Python, please go to the following link and follow the steps to download -> https://www.python.org/downloads/
- Secondly, once Python is successfully installed, install pip by following the steps mentioned in the following link -> https://pip.pypa.io/en/stable/installation/
- Lastly, install Django by opening the command prompt on your machine and type the following:
- For Windows -> py -m pip install Django
- For Mac/Linus -> py -m pip install Django

- Once Python, pip, and django have been installed, the project can be run

## Running the Website
1. Open up the command prompt on your pc and go to the project directory where '/website2' is located
2. Type in the command prompt the following:
```
python manage.py runserver
```

This will start the local host server to start the webpage
4. The command prompt will mention "Starting development server at http://127.0.0.1:8000/" or something similar. Please type in the URL mentioned there into a web browser to open up the webpage
5. To access the admin page to add/delete/view products and inventory amounts, please go to http://127.0.0.1:8000/admin/ . To go to a webpage that just shows product and inventory amounts, please go to http://127.0.0.1:8000/inventory/
