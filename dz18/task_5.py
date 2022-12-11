import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gitarist",
    database="my_first_db"
    )

mycursor = mydb.cursor()
sql = "INSERT INTO student (id, name) VALUES (%s, %s)"
val = ("01", "John")
mycursor.execute(sql, val)
sql = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
val = ("01", "John", "10000")
mycursor.execute(sql, val)
mydb.commit()
print("We made", mycursor.rowcount, "records")