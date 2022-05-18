# function to update review
import mysql.connector

def update_review(ISBN_,review_):
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor = bookDb.cursor() 
    update_query = "UPDATE books SET review = %s  WHERE ISBN = %s"
    values = (review_, ISBN_)
    mycursor.execute(update_query,values)
    bookDb.commit()
    