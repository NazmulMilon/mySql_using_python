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

sql = "INSERT INTO teachers (name, id, age, salary) \
    VALUES (%s, %s, %s, %s)"
val = [("Rupol Ahmed", 115, 29, 30000),
       ("Rupol Hasan", 116, 30, 35000),
       ("Milon Sarker", 117, 31, 39000),
       ("Sarker Sarker", 118, 32, 50000)]
cursor_object.executemany(sql, val)
dataBase.commit()


cursor_object.execute("SHOW DATABASES")
for db in cursor_object:
    print(db)
'''
('information_schema',)
('abc',)
('database_create',)
('db_school',)
('dbname',)
('gfg',)
('my_db',)
('my_dbs',)
('mydatabase',)
('mysql',)
('performance_schema',)
('quantibly',)
('sys',)
'''
