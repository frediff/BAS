# function to update rack_number
import mysql.connector

def update_rack_number(ISBN_,rack_number_):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    update_query = "UPDATE books SET rack_number = %s  WHERE ISBN = %s"
    values = (rack_number_, ISBN_)
    mycursor.execute(update_query,values)
    bookDb.commit()
    