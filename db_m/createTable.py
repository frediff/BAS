import mysql.connector

SalesDb = mysql.connector.connect(host="localhost",user="root",password="Book@123", database = "SalesDatabase")

mycursor = SalesDb.cursor()

mycursor.execute("CREATE TABLE Sale (ISBN VARCHAR(1023), N_copies int, Price VARCHAR(255), Date_ VARCHAR(255))")