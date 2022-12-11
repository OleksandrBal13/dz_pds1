import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gitarist",
    database="my_first_db"
    )

mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE student MODIFY id INT AUTO_INCREMENT PRIMARY KEY")