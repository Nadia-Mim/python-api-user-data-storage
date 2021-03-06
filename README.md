# python-api-user-data-storage


### Language: Python

Python version: 3.7.7 64 bit.

The required Python version is 3.7 or higher. To download visit [python website](https://www.python.org/downloads/) and download python in your device.


## About the project

This is an api based application. In this project one can create two types of user data: Parent type and Child type. The parent data includes their first name, last name and address [street, city, state and zip]. However the child is not allowed to have a address of their own. They belong to a parent and their data includes their first name, last name and refers to their respective parent. The database stores parent data in parentType table and child data in childType table. This app adds user data and perform update, delete and read operations.

## How to run

This project was done using Visual Studio Code. I have used the Flask, Flask-RESTful, Flask-SQLAlchemy, SQLAlchemy for this project. I have used the sqlite database. The project contains the following files -
* main.py
* test.py
* requirements.txt and
* README.md

Download the project in your device and unzip the files. To run this project install the following requirements using pip.
* aniso8601==8.0.0
* click==7.1.2
* Flask==1.1.2
* Flask-RESTful==0.3.8
* Flask-SQLAlchemy==2.4.3
* itsdangerous==1.1.0
* Jinja2==2.11.2
* MarkupSafe==1.1.1
* pytz==2020.1
* six==1.15.0
* SQLAlchemy==1.3.18
* Werkzeug==1.0.1

All these files are in the [requirements.txt](https://github.com/Nadia-Mim/python-api-user-data-storage/blob/main/requirements.txt) file. Open windows command prompt and navigate to the project folder or if you are using Visual Studio Code just open the folder in VS code and open terminal. Type 

`pip install -r requirements.txt`

and it will install the above requirements in your environment.

In VS code I have installed the following extensions-
* Pylance v2022.2.4
* Python v2022.0.1814523869
* SQLite Viewer v0.1.5
* Visual Studio IntelliCode v1.2.17

In order to run the project, in the terminal of VS code or in the command prompt type 

`python main.py`

and press enter. This will start the server and create database named "userData" and create the tables. Use the SQLite Viewer to view the database.

**Comment out** the line `db.create_all()` once the server starts running.

Next in order to test the application open another terminal in VS code or in the command prompt and type

`python test.py`

This will test the application for creating user data, deleting user data, updating user data and reading user data for both parents and child. It also performs error checking test as well.

**press 'enter' or any other key** in the keyboard each time after the output is shown in the terminal for the test cases.

The output of the data can be seen in the test.py command prompt and the main.py command prompt display http status code for each of the operation.

