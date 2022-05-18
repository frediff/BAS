import mysql.connector

bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123")
mycursor = bookDb.cursor()

mycursor.execute("CREATE DATABASE bookDatabase")
