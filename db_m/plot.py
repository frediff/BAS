import matplotlib.pyplot as plt
import numpy as np
import mysql.connector

# Connecting to the server
SalesDb = mysql.connector.connect(host="localhost", user="root", password="Book@123", database="SalesDatabase")
    
mycursor = SalesDb.cursor()

# Selecting the rows of the Table "Sale"
mycursor.execute("SELECT * from Sale")

myresult = mycursor.fetchall()

def stats(ISBN):
    date = []
    sold = []
    for a in myresult:
        if(a[0] == ISBN):
            sold.append(a[1])
            date.append(a[3])
            
    result = dict()
    for x,y in zip(date,sold):
         if x in result:
          result[x] += y
         else :
          result[x] = y
 
    plt.bar(result.keys(),result.values())
    plt.xlabel("Date")
    plt.ylabel("Sales")

    plt.show()

#stats("1234567890")
