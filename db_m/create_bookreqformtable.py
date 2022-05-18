import mysql.connector

#connecting to book requisition form database
bookreqformDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookReqform")
mycursor = bookreqformDb.cursor()

#creating table to store book details
mycursor.execute("CREATE TABLE bookrequests (ISBN BIGINT UNSIGNED, book_title VARCHAR(255), author VARCHAR(255), language_ VARCHAR(255),  genre VARCHAR(255), review VARCHAR(255), rating TINYINT )")
