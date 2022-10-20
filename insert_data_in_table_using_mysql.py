# importing required libraries
import mysql.connector

# dbname = input('Please enter the name of database : ')

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="15101997",
    database="db_school",
    port='3306'
)
# print(dataBase)

# preparing a cursor object
cursor_object = dataBase.cursor()

# creating database
# cursor_object.execute("CREATE DATABASE IF NOT EXISTS %s" % dbname)
# cursor_object.execute("CREATE DATABASE db_school")

# cursor_object.execute("SHOW DATABASES")


# cursor_object.execute("CREATE TABLE teachers (name VARCHAR(255), id INTEGER(10), age INTEGER(10), salary INTEGER(10))")

# cursor_object.execute(SHOW TABLES)

# Disconnecting from the server
# dataBase.close()

sql = "INSERT INTO students (id, name, age, phone) \
    VALUES (%s, %s, %s, %s)"
val = [(10, "Rupol Ahmed", 20, 123456),
       (11, "ABC Khan", 21, 123456),
       (12, "Monaem khan", 23, 123456),
       (13, "nazmul Sarker", 24, 789654)]
# cursor_object.execute(sql, val) '''insert single row values in sql'''
cursor_object.executemany(sql, val)
dataBase.commit()
