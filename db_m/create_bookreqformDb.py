import mysql.connector

bookreqformDb = mysql.connector.connect(host="localhost",user="root",password="Book@123")
mycursor = bookreqformDb.cursor()

mycursor.execute("CREATE DATABASE bookReqform")