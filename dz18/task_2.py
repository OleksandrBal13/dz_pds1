import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gitarist",
    database="my_first_db"
    )

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE student (id int(100), name VARCHAR(255))")