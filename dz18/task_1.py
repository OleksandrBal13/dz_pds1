import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gitarist",
    )

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE my_first_db")