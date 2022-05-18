# Creates book data base and a table called "books" to store the database of books
import mysql.connector

#creating book database
bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
mycursor = bookDb.cursor()

#creating table to store book details
mycursor.execute("CREATE TABLE books (ISBN BIGINT UNSIGNED NOT NULL, book_title VARCHAR(255), author VARCHAR(255), language_ VARCHAR(255),  genre VARCHAR(255), price SMALLINT UNSIGNED, copies SMALLINT UNSIGNED, rack_number SMALLINT UNSIGNED, vendor_name VARCHAR(255), vendor_mailID VARCHAR(255), vendor_mobile BIGINT UNSIGNED, average_procurement_time INT UNSIGNED, inventory_level INT UNSIGNED, review VARCHAR(255), rating TINYINT, PRIMARY KEY (ISBN))")
