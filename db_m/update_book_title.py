# function to update book title
import mysql.connector

def update_book_title(ISBN_,book_title_):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    update_query = "UPDATE books SET book_title = %s  WHERE ISBN = %s"
    values = (book_title_, ISBN_)
    mycursor.execute(update_query,values)
    bookDb.commit()
    