import mysql.connector

mydb=mysql.connector.connect(
    host="local host",
    user="root",
    passwoard="root",
    database="rkce"
)
print(mydb)