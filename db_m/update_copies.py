# function to update book copies
import mysql.connector

def update_copies(ISBN_,copies_):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    update_query = "UPDATE books SET copies = %s  WHERE ISBN = %s"
    values = (copies_, ISBN_)
    mycursor.execute(update_query,values)
    bookDb.commit()
    