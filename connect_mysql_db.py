# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="15101997",
    port='3306'
)

print(dataBase)

# Disconnecting from the server
dataBase.close()
