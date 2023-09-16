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
<table>
  <tr>
    <td>Django</td>
    <td>djangorestframework</td>
    <td>sqlparse</td>
    <td>validate-docbr</td>
  </tr>
  <tr>
    <td>4.2.5</td>
    <td>3.14.0</td>
    <td>0.4.4</td>
    <td>1.10.0</td>
  </tr>
</table>

## How to run app:
+ 1 - Use the "pip install -r requirements.txt" command to install all of the Python modules
+ 2 - Migrations and migrate with the commands "makemigrations" and "migrate" on the command line
+ 3 - Create SuperUser with the command: "python manage.py createsuperuser"
+ 4 - Run the populate_script.py file to populate your database
+ 5 - Use the "python manage.py runserver" command to init your sever and get your API running
