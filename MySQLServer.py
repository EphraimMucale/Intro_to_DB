import mysql.connector

mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "74pages@A12mucale.1998"
    database = "employees"
    
)
mycursor = mydatabase.cursor()
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)
