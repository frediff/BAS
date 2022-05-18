# function to update employee name
import mysql.connector

def update_employee_name(Id_,_name_):
    employeeDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="employeeDatabase")
    mycursor = employeeDb.cursor() 
    update_query = "UPDATE employee SET name_ = %s  WHERE Id = %s"
    values = (_name_,Id_)
    mycursor.execute(update_query,values)
    employeeDb.commit()