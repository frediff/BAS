import datetime
import time
import mysql.connector

def get_inventory_level(ISBN_):
    today = datetime.date.today()

    last_week = today - datetime.timedelta(days=14)
    ltw = last_week.strftime('%d-%m-%Y')
    SalesDb = mysql.connector.connect(host="localhost", user="root", password="Book@123", database="SalesDatabase")
    mycursor_1 = SalesDb.cursor()
    search_query_1 = "SELECT * from Sale WHERE ISBN = %s"
    values = (ISBN_,)
    mycursor_1.execute(search_query_1, values )
    myresult_1 = mycursor_1.fetchall()
    sum = 0
    f1 = time.strptime(ltw, "%d-%m-%Y")
    for a in myresult_1:
        f2 = time.strptime(a[3], "%d-%m-%Y")
        if(f2 >= f1):
            sum += int(a[1])
    bookDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="bookDatabase")
    mycursor_2 = bookDb.cursor()
    search_query_2 = "SELECT average_procurement_time FROM books WHERE ISBN = %s"
    mycursor_2.execute(search_query_2,values)
    myresult_2 = mycursor_2.fetchall()
    if(myresult_2):
     inventory_level = sum * myresult_2[0][0]
    else:
     inventory_level = 0  
    update_query = "UPDATE books SET inventory_level = %s  WHERE ISBN = %s"
    values_2 = (inventory_level, ISBN_)
    mycursor_2.execute(update_query,values_2)
    bookDb.commit()  
    return inventory_level

        
