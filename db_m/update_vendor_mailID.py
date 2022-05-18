import mysql.connector

def update_vendor_mailID(ISBN_,vendor_mailID_):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    update_query = "UPDATE books SET vendor_mailID = %s  WHERE ISBN = %s"
    values = (vendor_mailID_, ISBN_)
    mycursor.execute(update_query,values)
    bookDb.commit()
    