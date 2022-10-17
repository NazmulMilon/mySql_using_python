import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="15101997",
    database="db_school"
)

cursor_object = dataBase.cursor()

query = "SELECT * FROM students ORDER BY name DESC"
cursor_object.execute(query)

my_result = cursor_object.fetchall()

for data in my_result:
    print(data)

dataBase.close()

