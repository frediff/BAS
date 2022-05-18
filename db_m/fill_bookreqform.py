#function for inserting new book to the book requisition form database
import mysql.connector

#function for checking whether the ISBN is correct or not
def check_ISBN (ISBN):
    if((len(str(ISBN)) == 10 or len(str(ISBN)) == 13) and (str(ISBN).isdigit())):
        return True
    else:
        return False

def fill_bookreqform(ISBN, book_title, author, language_, genre, review = "-", rating = -1):
   # checking ISBN for corectness
   if(not check_ISBN(ISBN)):
    return "Please enter valid ISBN Number!!"
   bookreqformDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookReqform")
   mycursor = bookreqformDb.cursor() 
   #inserting book into the database
   search_query = "SELECT * FROM bookrequests WHERE book_title = %s AND author = %s "
   values = (book_title,author)
   mycursor.execute(search_query,values)
   myresult = mycursor.fetchall() 
   if myresult:
       return "The details of the book entered are aleady recorded!!"
   insert_query = "INSERT INTO bookrequests (ISBN, book_title, author, language_, genre, review, rating) VALUES (%s,%s,%s,%s,%s,%s,%s)"
   record = (ISBN, book_title, author, language_, genre, review, rating)
   mycursor.execute(insert_query, record)
   bookreqformDb.commit()
   if bookreqformDb.is_connected():
       mycursor.close()
       bookreqformDb.close()
   return "Book request is succesfully recorded!!"
       
