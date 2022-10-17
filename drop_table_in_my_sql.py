
import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="15101997",
    database="db_school"
)

cursor_object = dataBase.cursor()

# statement = "DROP DATABASE dbname"
statement = "DROP TABLE students"
cursor_object.execute(statement)

# cursor_object.execute('SHOW TABLE')
# for data in cursor_object:
#     print(data)

dataBase.close()

