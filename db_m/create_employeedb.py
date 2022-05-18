import mysql.connector

employeeDb = mysql.connector.connect(host="localhost",user="root",password="Book@123")
mycursor = employeeDb.cursor()

mycursor.execute("CREATE DATABASE employeeDatabase")