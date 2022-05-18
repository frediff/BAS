import mysql.connector

def get_book_price(Isbn):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    search_query = "SELECT * FROM books WHERE ISBN = %s"
    values = (Isbn,)
    mycursor.execute(search_query,values)
    myresult = mycursor.fetchall()
    return myresult[0][5]
