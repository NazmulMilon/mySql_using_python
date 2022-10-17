

import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="15101997",
    database="db_school"
)

cursor_object = dataBase.cursor()

# statement = "DROP DATABASE dbname"
# statement = "UPDATE students SET age =30 WHERE name='Milon'"
statement = "UPDATE students SET name='S.M. Nazmul Hasan' WHERE name='Milon'"
cursor_object.execute(statement)
dataBase.commit()

# cursor_object.execute('SHOW TABLE')
# for data in cursor_object:
#     print(data)

dataBase.close()

