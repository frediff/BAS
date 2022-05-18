# function to search book by author
import mysql.connector

def search_book_by_author(Author):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    search_query = "SELECT * FROM books WHERE author LIKE '%"+Author+"%'"
    mycursor.execute(search_query)
    myresult = mycursor.fetchall()
    return myresult
