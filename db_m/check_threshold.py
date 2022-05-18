import mysql.connector

def check_threshold():
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    search_query = "SELECT * FROM books WHERE copies<5"
    mycursor.execute(search_query)
    myresult = mycursor.fetchall()
    return myresult