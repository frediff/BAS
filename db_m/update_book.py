#function for inserting new book to the database
import mysql.connector
#function for checking whether the ISBN is correct or not
def check_ISBN (ISBN):
    if((len(str(ISBN)) == 10 or len(str(ISBN)) == 13) and (str(ISBN).isdigit())):
        return True
    else:
        return False
    
# function for checking whether the mobile number of the customer is correct or not
def check_vendor_mobile(vendor_mobile):
    if( len(str(vendor_mobile)) == 10 and str(vendor_mobile).isdigit()):
        return True
    else:
        return False

def update_book(ISBN, book_title, author, language_, genre, price, copies, rack_number, vendor_name, vendor_mailID, vendor_mobile,  review = "-", rating = -1, average_procurement_time = 7, inventory_level = 0):
   # checking ISBN for corectness
   if(not check_ISBN(ISBN)):
    return "Please enter valid ISBN Number!!"
   #checking mobile for correctness
   if(not check_vendor_mobile(vendor_mobile)):
    return "Please enter valid Mobile Number!!"
   bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
   mycursor = bookDb.cursor() 
   #inserting book into the database
   delete_query = "DELETE FROM books WHERE ISBN = %s"
   values = (ISBN,)
   mycursor.execute(delete_query,values)
   

   insert_query = "INSERT INTO books (ISBN, book_title, author, language_, genre, price, copies, rack_number, vendor_name, vendor_mailID, vendor_mobile, review, rating, average_procurement_time, inventory_level) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
   record = (ISBN, book_title, author, language_, genre, price, copies, rack_number, vendor_name, vendor_mailID, vendor_mobile, review, rating, average_procurement_time, inventory_level)
   mycursor.execute(insert_query, record)
   bookDb.commit()
   if bookDb.is_connected():
       mycursor.close()
       bookDb.close()
   return "Book data is succesfully recorded!!"
       
