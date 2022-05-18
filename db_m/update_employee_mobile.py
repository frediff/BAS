# function to update emoployee mobile
import mysql.connector

def update_employee_mobile(Id_,mobile_):
    employeeDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="employeeDatabase")
    mycursor = employeeDb.cursor() 
    update_query = "UPDATE employee SET mobile = %s  WHERE Id = %s"
    values = (mobile_,Id_)
    mycursor.execute(update_query,values)
    employeeDb.commit()
    