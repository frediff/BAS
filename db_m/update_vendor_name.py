import mysql.connector

def update_vendor_name(ISBN_,vendor_name_):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    update_query = "UPDATE books SET vendor_name = %s  WHERE ISBN = %s"
    values = (vendor_name_, ISBN_)
    mycursor.execute(update_query,values)
    bookDb.commit()