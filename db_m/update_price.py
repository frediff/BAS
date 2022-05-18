import mysql.connector

def update_price(ISBN_,price_):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    update_query = "UPDATE books SET price = %s  WHERE ISBN = %s"
    values = (price_, ISBN_)
    mycursor.execute(update_query,values)
    bookDb.commit()
    