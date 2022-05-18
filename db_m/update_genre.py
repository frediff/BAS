import mysql.connector

def update_genre(ISBN_,genre_):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    update_query = "UPDATE books SET genre = %s  WHERE ISBN = %s"
    values = (genre_, ISBN_)
    mycursor.execute(update_query,values)
    bookDb.commit()
    