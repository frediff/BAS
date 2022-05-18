import mysql.connector

def search_book_by_title(book_title_):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    search_query = "SELECT * FROM books WHERE book_title LIKE '%"+book_title_+"%'"
    mycursor.execute(search_query)
    myresult = mycursor.fetchall()
    return myresult
    
