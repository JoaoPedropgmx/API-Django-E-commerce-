<h1>E-commerce-API</h1>

> Status: Devolping ⚠️

### a API using django rest framework to simulate a e-commerce with users, products and sellings.

## Commands and Fields:

+ View Sellings by User:  clientes/<int:pk>/compras
+ View Sellings by Products: produtos/<int:pk>/compras
+ View User by id: clientes/<int:pk>/
+ View Products by id: produtos/<int:pk>/


## Every User has the following fields:
+ Name
+ Email
+ CPF
+ rg
+ cellphone
+ active or not

Technologies used:
+ asgiref==3.7.2
+ astroid==2.4.2
+ colorama==0.4.6
+ Django==4.2.5
+ django-filter==23.2
+ djangorestframework==3.14.0
+ Faker==19.5.0
+ isort==4.3.21
+ lazy-object-proxy==1.4.3
+ mccabe==0.6.1
+ pylint==2.5.3
+ python-dateutil==2.8.2
+ pytz==2020.1
+ six==1.15.0
+ sqlparse==0.4.4
+ toml==0.10.1
+ tzdata==2023.3
+ validate-docbr==1.10.0
+ wrapt==1.12.1

## How to run app:
+ 1 - Use the "pip install -r requirements.txt" command to install all of the Python modules
+ 2 - Migrations and migrate with the commands "makemigrations" and "migrate" on the command line
+ 3 - Create SuperUser with the command: "python manage.py createsuperuser"
+ 4 - Run the populate_script.py file to populate your database
+ 5 - Use the "python manage.py runserver" command to init your sever and get your API running
