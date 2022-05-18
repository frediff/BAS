import mysql.connector

def update_vendor_mobile(ISBN_,vendor_mobile_):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    update_query = "UPDATE books SET vendor_mobile = %s  WHERE ISBN = %s"
    values = (vendor_mobile_, ISBN_)
    mycursor.execute(update_query,values)
    bookDb.commit()
    