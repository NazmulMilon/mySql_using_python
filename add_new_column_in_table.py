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
query = "ALTER TABLE students ADD section VARCHAR(100)"
cursor_object.execute(query)

dataBase.commit()

cursor_object.execute("SHOW TABLES")
for db in cursor_object:
    print(db)
'''
('teachers',)
'''
