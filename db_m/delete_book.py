# function to delete book based on ISBN
import mysql.connector

def delete_book(ISBN_):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    delete_query = "DELETE FROM books WHERE ISBN = %s"
    values = (ISBN_,)
    mycursor.execute(delete_query,values)
    bookDb.commit()