import mysql.connector

def search_book_by_genre(Genre):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    search_query = "SELECT * FROM books WHERE genre LIKE '%"+Genre+"%'"
    mycursor.execute(search_query)
    myresult = mycursor.fetchall()
    return myresult
