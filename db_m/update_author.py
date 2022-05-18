import mysql.connector

def update_author(ISBN_,author_):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    update_query = "UPDATE books SET author = %s  WHERE ISBN = %s"
    values = (author_, ISBN_)
    mycursor.execute(update_query,values)
    bookDb.commit()
    