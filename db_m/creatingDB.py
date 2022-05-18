import mysql.connector

SalesDb = mysql.connector.connect(host="localhost",user="root",password="Book@123")

mycursor = SalesDb.cursor()

mycursor.execute("CREATE DATABASE SalesDatabase")