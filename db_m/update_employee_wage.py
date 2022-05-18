# function to update employee wage
import mysql.connector

def update_employee_wage(Id_,wage_):
    employeeDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="employeeDatabase")
    mycursor = employeeDb.cursor() 
    update_query = "UPDATE employee SET wage = %s  WHERE Id = %s"
    values = (wage_,Id_)
    mycursor.execute(update_query,values)
    employeeDb.commit()