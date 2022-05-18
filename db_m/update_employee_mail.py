# function to update employee mail ID
import mysql.connector

def update_employee_mail(Id_,mail_):
    employeeDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="employeeDatabase")
    mycursor = employeeDb.cursor() 
    update_query = "UPDATE employee SET mailId = %s  WHERE Id = %s"
    values = (mail_,Id_)
    mycursor.execute(update_query,values)
    employeeDb.commit()