# importing required libraries
import mysql.connector

# dbname = input('Please enter the name of database : ')

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="15101997",
    database="db_school"
)
# print(dataBase)

# preparing a cursor object
cursor_object = dataBase.cursor()

# creating database
# cursor_object.execute("CREATE DATABASE IF NOT EXISTS %s" % dbname)
# cursor_object.execute("CREATE DATABASE dbname")

# cursor_object.execute("SHOW DATABASES")


# cursor_object.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
# cursor_object.execute(students)

# Disconnecting from the server
# dataBase.close()

sql = "INSERT INTO students (name, age) \
    VALUES (%s, %s)"
val = [("Nazim", 24),
       ("Hasan", 26),
       ("Milon", 27),
       ("Sarker", 28)]
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
