import mysql.connector

def update_vendor_mobile(ISBN_,rating_):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    update_query = "UPDATE books SET rating = %s  WHERE ISBN = %s"
    values = (rating_, ISBN_)
    mycursor.execute(update_query,values)
    bookDb.commit()