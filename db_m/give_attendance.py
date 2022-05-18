#function for taking attendance from employee
import mysql.connector
from datetime import datetime

def give_attendance(Id,status_):
    #getting present date
    date_now = datetime.now()
    formatted_date = date_now.strftime('%Y-%m-%d')
    employeeDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="employeeDatabase")
    mycursor = employeeDb.cursor()
    #updating attendance
    insert_query = "INSERT INTO attendance (Id,date_,status_) VALUES (%s,%s,%s)"
    record = (Id,formatted_date,status_)
    mycursor.execute(insert_query, record)
    employeeDb.commit()
    if employeeDb.is_connected():
           mycursor.close()
           employeeDb.close()