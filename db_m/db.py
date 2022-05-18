from datetime import datetime
import mysql.connector


DATE = datetime.now()
Formatted_date = DATE.strftime('%d-%m-%Y')


def SaleUpdate(ISBN_, COPIES, price,  __date_=Formatted_date):

    SalesDb = mysql.connector.connect(
        host="localhost", user="root", password="Book@123", database="SalesDatabase")
    mycursor = SalesDb.cursor()
    sql = "INSERT INTO Sale (ISBN, N_copies, Price, Date_) VALUES (%s, %s, %s, %s)"
    val = (ISBN_, COPIES, price, __date_)
    mycursor.execute(sql, val)
    SalesDb.commit()

    if SalesDb.is_connected():
        mycursor.close()
        SalesDb.close()


# SaleUpdate("9876543210", 23, 345, "12-01-2002")
# SaleUpdate("9876556757210", 56, 1005, "23-12-2005")
# SaleUpdate("9876543254", 9, 600, "31-03-2006")
# SaleUpdate("9876543211", 25, 543, "08-09-2007")
# SaleUpdate("9876543221345", 3, 945, "10-01-2012")
# SaleUpdate("9876543221123", 42, 973, "10-01-2012")
# SaleUpdate("9876543212", 32, 125, "15-08-2012")
# SaleUpdate("9876543228", 27, 345, "12-05-2021")
# SaleUpdate("9876512123110", 43, 945, "12-01-2022")
# SaleUpdate("9876543221123", 18, 973, "12-01-2022")
# SaleUpdate("9876543221123", 59, 973, "12-02-2022")
# SaleUpdate("9876545510", 29, 395, "12-03-2022")
# SaleUpdate("9876543221123", 3, 973, "05-04-2022")
# SaleUpdate("9876543221300", 2, 999)
# SaleUpdate("9876543221729", 7, 567)
# SaleUpdate("9876543221600", 64, 873)

# SaleUpdate("9876543221123", 5, 973)
# SaleUpdate("9876543221123", 9, 973)
# SaleUpdate("9876543221123", 7, 973)
# SaleUpdate("9876543221123", 12, 973)
