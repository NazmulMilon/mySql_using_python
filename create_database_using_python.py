
# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="15101997",
    port='3306',
)

# preparing a cursor object
cursor_object = dataBase.cursor()

# creating database
cursor_object.execute("CREATE DATABASE library_db")

# cursor_object.execute("SHOW DATABASES")
# for db in cursor_object:
#     print(db)