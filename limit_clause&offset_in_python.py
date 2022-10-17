

import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="15101997",
    database="db_school"
)

cursor_object = dataBase.cursor()

# statement = "DROP DATABASE dbname"
# statement = "SELECT * FROM students LIMIT 2"
statement = "SELECT * FROM students LIMIT 2 OFFSET 1"
cursor_object.execute(statement)
fetch_data = cursor_object.fetchall()

for data in fetch_data:
    print(data)

# dataBase.close()

