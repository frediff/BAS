import mysql.connector

def update_language(ISBN_,_language_):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    update_query = "UPDATE books SET language_ = %s  WHERE ISBN = %s"
    values = (_language_, ISBN_)
    mycursor.execute(update_query,values)
    bookDb.commit()
    